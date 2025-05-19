#!/usr/bin/env python
# coding: utf-8

# # DDM

# In[46]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.stats import t
from sklearn.linear_model import LinearRegression
import os
from scipy.optimize import minimize
import glob


##### LOAD PARTICIPANT DATA ####### 


# Get data file names
cur_path = os.getcwd()
filenames = glob.glob(cur_path + "/data/*.csv")
# Read dframes into a list
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))
    
    
filt_dfs = []
x = []
# concat all dframes into one dframe
for d in dfs:
    my_df = d.filter(items=['congruent', 'Rand Tim', 'key_resp.rt','block_num'])
    # drop na, only 10s
    filt_dfs.append(my_df.dropna())
    x.append(len(my_df.dropna(subset = ['congruent'])) - len(my_df.dropna(subset = ['key_resp.rt'])))

## concat #
full_dat = pd.concat(filt_dfs)


# Restructure full_dat to match df
# Rename columns
full_dat.rename(columns={
    'key_resp.rt': 'rt',
    'Rand Tim': 'onset'
}, inplace=True)

# Map 'congruent' to 'trial_type'
full_dat['trial_type'] = full_dat['congruent'].map({0.0: 'invalid', 1.0: 'valid'})

# Convert 'block_num' to 'task'
# Assuming '5s' corresponds to 5, and you want to convert it to an integer or another value
full_dat['task'] = full_dat['block_num'].str.replace('s', '').astype(int) 

# Drop or reorder columns if necessary
participant_data = full_dat[['rt', 'onset', 'trial_type', 'task']]

##################
################## FUNCTIONS ##################
##################

def biased_random():
    return np.random.choice([0, 1], p=[0.25, 0.75])

def signal(time, onset):
    return 1 if time >= onset else 0


# Cost function (i.e. cost of attending)
def cost_func(p1, x): # this produced the upwards towards the end of the 10th
    max_value = 10
    c_func = math.exp(p1 * x - 2) # range .2-.45
    cost = c_func / max_value
    return cost
## Benefit of attending
def benefit(p1, x, interval_end):
    x = x / interval_end
    return 1 / (1 + math.exp(-p1 * x)) # range 1-10
## Benefit - cost
def gain(onset, task, prob_param, cost_param):
    g_x = (benefit(prob_param, onset, task) - cost_func(cost_param, onset))
    return g_x


# Cost function to minimize
def cost_function(params, actual_data):
    decision_threshold, initial_bias, prob_param, cost_param, noise_param = params
    print(params)
    simulated_data = run_ddm_simulation(initial_bias, decision_threshold, prob_param, cost_param, noise_param, actual_data)  # Your DDM simulation function
    

    # Calculate the error between actual and simulated reaction times
    # Use a filtering approach to separate the error by trial_type and task if needed
    error = 0

    # Iterate over each unique combination of trial_type and task
    for trial_type in actual_data['trial_type'].unique():
        for task in actual_data['task'].unique():
            # Filter the data for this condition
            actual_rt = actual_data[(actual_data['trial_type'] == trial_type) & 
                                    (actual_data['task'] == task)]['rt']
            simulated_rt = simulated_data[(simulated_data['trial_type'] == trial_type) & 
                                          (simulated_data['task'] == task)]['rt']
            #print('actual',actual_rt.values)
            #print('\nsim',simulated_rt.values)
                                                                        
                                                            
            # Compute the error for this condition
            if len(actual_rt) > 0 and len(simulated_rt) > 0:
                # Compute the mean and variance for actual and simulated RTs
                mean_error = np.mean((actual_rt.mean() - simulated_rt.mean()) ** 2)
                variance_error = np.mean((actual_rt.var() - simulated_rt.var()) ** 2)
                
                # Combine the errors (you can adjust the weights if needed)
                condition_error = mean_error + variance_error
                error += condition_error
                
                
    print('error:', error)
    return error



# Simulation function (from your provided code)
def run_ddm_simulation(initial_bias, decision_threshold, prob_param, cost_param, noise_param, actual_data):
    
    # Define DDM parameters
    decision_threshold = decision_threshold  # a: Decision threshold
    initial_bias = initial_bias       # z: Starting point of the evidence accumulator
    prob_param = prob_param
    cost_param = cost_param
    noise_param = noise_param
    dt = 0.01                 # Time step for the simulation
    
    reaction_times = []
    onset_times = []
    choices = []
    task_len = []
    num_missed = 0

    # Simulate DDM for each trial
    for index, row in actual_data.iterrows():
        evidence = initial_bias
        trial_type = row['trial_type']
        onset = row['onset']
        non_decision_time = onset
        task = row['task']
        time = 0.0

        # Simulate evidence accumulation process until a boundary is reached
        while np.abs(evidence) < decision_threshold:
            stim_on = signal(time, onset)
            if stim_on == 1:
                drift_rate = gain(onset, task, prob_param, cost_param) if trial_type == 'valid' else -gain(onset, task, prob_param, cost_param)
                # Update evidence with drift and noise
                evidence += drift_rate * dt + np.random.normal(0, np.sqrt(noise_param))
            else:
                drift_rate = 0
                # Update evidence with drift and noise
                evidence += drift_rate * dt + np.random.normal(0, np.sqrt(0.00001))
            
            time += dt
            if time > 50: break # destroy if running for too long

        ## record RT 
        rt = time - non_decision_time
        if rt < 0 or np.isnan(rt): rt = 50 # penalize if rt is negative or not a value
        if rt > 1 : num_missed+=1
        if rt > 10: rt = 50    # penalize if rt is not a reasonable miss
        

        # Record reaction time and choice
        reaction_times.append(rt) # add variance in RT according to exp data
        onset_times.append(onset)
        choices.append(trial_type)
        task_len.append(task)
            

    # Create DataFrame
    df = pd.DataFrame({
        'rt': np.array(reaction_times),
        'onset': np.array(onset_times),
        'trial_type': np.array(choices),
        'task': np.array(task_len)
    })

        
    return df

####################################
# # FIT
####################################



# Assuming you have actual participant data in a DataFrame called participant_data
actual_data = participant_data  # e.g., your DataFrame with reaction times and other metrics




# Define the ranges for parameters
'''
decision_thresholds = np.linspace(0.4, 0.7, 10)  # 10 values from 0.0 to 0.7 # INITIAL: np.linspace(0.5, 0.7, 10)
initial_biases = np.linspace(0.05, 0.4, 10)        # 10 values from 0.1 to 0.9 # INITIAL: np.linspace(0.1, 0.5, 10) 
prob_params = np.linspace(5.0, 20.0, 5)           # 10 values from 0.0 to 1.0
cost_params = np.linspace(0.3, 0.6, 10)            # 10 values from 0.0 to 0.1
noise_params = np.array([.01, .001, .0001, .00001])
'''
decision_thresholds = np.linspace(0.3, 0.6, 5)  # 10 values from 0.0 to 0.7 # INITIAL: np.linspace(0.5, 0.7, 10)
initial_biases = np.linspace(0.05, 0.3, 5)        # 10 values from 0.1 to 0.9 # INITIAL: np.linspace(0.1, 0.5, 10) 
prob_params = np.linspace(5, 10, 5)           # np.linspace(5.0, 15.0, 4) 
cost_params = np.linspace(0.2, 0.45, 5)            # 10 values from 0.3 to .6 BEFORE then .4 to .8 AFTER
noise_params = np.array([.001, .0001]) # np.array([.01, .001, .0001, .00001])

best_cost = float('inf')
best_params = None
best_p_list = []

# Iterate through all combinations
for decision_threshold in decision_thresholds:
    for initial_bias in initial_biases:
        for prob_param in prob_params:
            for cost_param in cost_params:
                for noise_param in noise_params:
                    if initial_bias > decision_threshold:
                        print('skip')
                        continue

                    params = [decision_threshold, initial_bias, prob_param, cost_param, noise_param]
                    cost = cost_function(params, actual_data)

                    if cost < best_cost:
                        best_cost = cost
                        best_params = params
                        print(f'******NEW BEST PARAMS!*****\n {best_params}\n ')
                        best_p_list.append(best_params)
                        np.save('best_params_newcostfunc.npy', best_p_list)

print("Best Parameters:", best_params)
print("Best Cost Achieved:", best_cost)





