#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Thu Jul  7 17:44:55 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Packages # 
import random as rand
import numpy as np
from scipy.stats import uniform

# Vars # 
feedback = ""
block_num  =-1
run_num = 1

init_cue_time = 1
isi = 1 
present_time = 1
arr = [0,1,2,3]
rand.shuffle(arr)
## Functions ##
def rand_tim_10():
        return np.round(uniform.rvs(loc = .15, scale =9.85, size=1),4)[0]
def rand_tim_5():
        return np.round(uniform.rvs(loc = .15, scale =4.85, size=1),4)[0]
def rand_tim_3():
        return np.round(uniform.rvs(loc = .15, scale =2.85, size=1),4)[0]
def rand_tim_1():
        return np.round(uniform.rvs(loc = .15, scale =.85, size=1),4)[0]


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = '2-25_cond_decay_EYE'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/isaacchristian/Desktop/Princeton/RESEARCH/decay/task/2-25_cond_decay_EYE.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcome = visual.TextStim(win=win, name='welcome',
    text='Vigilant Attention Task',
    font='Arial',
    pos=(0, .25), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Push the space bar to begin the experiment',
    font='Arial',
    pos=(0, -.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
init_key_resp = keyboard.Keyboard()

# Initialize components for Routine "dir_10"
dir_10Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(.15, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='The target transparency change will occur between:\n\n\n\n\n\n\n\n\n\n\nPress Space to continue',
    font='Arial',
    pos=(0, 0), height=.043, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='0 and',
    font='Arial',
    pos=(-.075, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
texter = visual.TextStim(win=win, name='texter',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=.5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
left_star = visual.ShapeStim(
    win=win, name='left_star', vertices='star7',
    size=(.2,.2),
    ori=0, pos=(-.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[255,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
right_star = visual.ShapeStim(
    win=win, name='right_star', vertices='star7',
    size=(.2,.2),
    ori=0, pos=(.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,255,0], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
left_2 = visual.ShapeStim(
    win=win, name='left_2', vertices='star7',
    size=(.2,.2),
    ori=0, pos=(-.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[255,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
right_2 = visual.ShapeStim(
    win=win, name='right_2', vertices='star7',
    size=(.2,.2),
    ori=0, pos=(.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,255,0], fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)
key_resp = keyboard.Keyboard()

print('HEYYYYY')
print(arr)

# Initialize components for Routine "FB"
FBClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end_run"
end_runClock = core.Clock()
end = visual.TextStim(win=win, name='end',
    text='Run number        is over.',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(.085, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='Nice Job :)',
    font='Arial',
    pos=(0, -.1), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
init_key_resp.keys = []
init_key_resp.rt = []
_init_key_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcome, text_2, init_key_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *init_key_resp* updates
    waitOnFlip = False
    if init_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        init_key_resp.frameNStart = frameN  # exact frame index
        init_key_resp.tStart = t  # local t and not account for scr refresh
        init_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(init_key_resp, 'tStartRefresh')  # time at next scr refresh
        init_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(init_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(init_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if init_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = init_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _init_key_resp_allKeys.extend(theseKeys)
        if len(_init_key_resp_allKeys):
            init_key_resp.keys = _init_key_resp_allKeys[-1].name  # just the last key pressed
            init_key_resp.rt = _init_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if init_key_resp.keys in ['', [], None]:  # No response was made
    init_key_resp.keys = None
thisExp.addData('init_key_resp.keys',init_key_resp.keys)
if init_key_resp.keys != None:  # we had a response
    thisExp.addData('init_key_resp.rt', init_key_resp.rt)
thisExp.addData('init_key_resp.started', init_key_resp.tStartRefresh)
thisExp.addData('init_key_resp.stopped', init_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "dir_10"-------
        continueRoutine = True
        # update component parameters for each repeat
        daboi="yoo"
        trial_count = 0
        block_num = block_num +1
        print("RUN NUM",run_num)
        if arr[block_num] ==0:
            daboi="10s"
        elif arr[block_num] ==1:
            daboi="5s"
        elif arr[block_num]==2:
            daboi="3s"
        elif arr[block_num]==3:
            daboi="1s"
        else:
            daboi = "nuttin"
        text_3.setText(daboi
)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        dir_10Components = [text_3, key_resp_2, text_4, text_5]
        for thisComponent in dir_10Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        dir_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "dir_10"-------
        while continueRoutine:
            # get current time
            t = dir_10Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=dir_10Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in dir_10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "dir_10"-------
        for thisComponent in dir_10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blocks.addData('text_3.started', text_3.tStartRefresh)
        blocks.addData('text_3.stopped', text_3.tStopRefresh)
        blocks.addData('text_4.started', text_4.tStartRefresh)
        blocks.addData('text_4.stopped', text_4.tStopRefresh)
        blocks.addData('text_5.started', text_5.tStartRefresh)
        blocks.addData('text_5.stopped', text_5.tStopRefresh)
        # the Routine "dir_10" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=2, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('pdist_cond.csv'),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial"-------
            continueRoutine = True
            # update component parameters for each repeat
            texter.setText(attn_cue)
            left_2.setOpacity(left_ob)
            right_2.setOpacity(right_ob)
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # GENERAL # 
            start_stim_1 = init_cue_time + isi
            #####
            if arr[block_num] ==0:
                rand_tim = rand_tim_10()
            elif arr[block_num] ==1:
                rand_tim = rand_tim_5()
            elif arr[block_num]==2:
                rand_tim = rand_tim_3()
            elif arr[block_num]==3:
                rand_tim = rand_tim_1()
            # PROB # 
            #rand_tim = rand_tim_10()
            start_stim_1 = init_cue_time + isi
            end_cross = isi +rand_tim + present_time
            start_stim_2 = start_stim_1+rand_tim
            
            # add condition
            thisExp.addData("block_num", daboi);
                    
                    
            if trial_count< 1:
                print(trials.trialList)
                print('ayo')
                rand.shuffle(trials.trialList)
                print(trials.trialList)
            
            #tims = [1,2,3,4,5,7.5,10,12.5,15,20]
            #rand_tim = shuffle(tims)
            #print(int_list)
            #rand_tim = 1
            
            # keep track of which components have finished
            trialComponents = [texter, cross, left_star, right_star, left_2, right_2, key_resp]
            for thisComponent in trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "trial"-------
            while continueRoutine:
                # get current time
                t = trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *texter* updates
                if texter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    texter.frameNStart = frameN  # exact frame index
                    texter.tStart = t  # local t and not account for scr refresh
                    texter.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(texter, 'tStartRefresh')  # time at next scr refresh
                    texter.setAutoDraw(True)
                if texter.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > texter.tStartRefresh + init_cue_time-frameTolerance:
                        # keep track of stop time/frame for later
                        texter.tStop = t  # not accounting for scr refresh
                        texter.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(texter, 'tStopRefresh')  # time at next scr refresh
                        texter.setAutoDraw(False)
                
                # *cross* updates
                if cross.status == NOT_STARTED and tThisFlip >= init_cue_time-frameTolerance:
                    # keep track of start time/frame for later
                    cross.frameNStart = frameN  # exact frame index
                    cross.tStart = t  # local t and not account for scr refresh
                    cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                    cross.setAutoDraw(True)
                if cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cross.tStartRefresh + end_cross-frameTolerance:
                        # keep track of stop time/frame for later
                        cross.tStop = t  # not accounting for scr refresh
                        cross.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                        cross.setAutoDraw(False)
                
                # *left_star* updates
                if left_star.status == NOT_STARTED and tThisFlip >= start_stim_1-frameTolerance:
                    # keep track of start time/frame for later
                    left_star.frameNStart = frameN  # exact frame index
                    left_star.tStart = t  # local t and not account for scr refresh
                    left_star.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_star, 'tStartRefresh')  # time at next scr refresh
                    left_star.setAutoDraw(True)
                if left_star.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > left_star.tStartRefresh + rand_tim-frameTolerance:
                        # keep track of stop time/frame for later
                        left_star.tStop = t  # not accounting for scr refresh
                        left_star.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(left_star, 'tStopRefresh')  # time at next scr refresh
                        left_star.setAutoDraw(False)
                
                # *right_star* updates
                if right_star.status == NOT_STARTED and tThisFlip >= start_stim_1-frameTolerance:
                    # keep track of start time/frame for later
                    right_star.frameNStart = frameN  # exact frame index
                    right_star.tStart = t  # local t and not account for scr refresh
                    right_star.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_star, 'tStartRefresh')  # time at next scr refresh
                    right_star.setAutoDraw(True)
                if right_star.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > right_star.tStartRefresh + rand_tim-frameTolerance:
                        # keep track of stop time/frame for later
                        right_star.tStop = t  # not accounting for scr refresh
                        right_star.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(right_star, 'tStopRefresh')  # time at next scr refresh
                        right_star.setAutoDraw(False)
                
                # *left_2* updates
                if left_2.status == NOT_STARTED and tThisFlip >= start_stim_2-frameTolerance:
                    # keep track of start time/frame for later
                    left_2.frameNStart = frameN  # exact frame index
                    left_2.tStart = t  # local t and not account for scr refresh
                    left_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_2, 'tStartRefresh')  # time at next scr refresh
                    left_2.setAutoDraw(True)
                if left_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > left_2.tStartRefresh + present_time-frameTolerance:
                        # keep track of stop time/frame for later
                        left_2.tStop = t  # not accounting for scr refresh
                        left_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(left_2, 'tStopRefresh')  # time at next scr refresh
                        left_2.setAutoDraw(False)
                
                # *right_2* updates
                if right_2.status == NOT_STARTED and tThisFlip >= start_stim_2-frameTolerance:
                    # keep track of start time/frame for later
                    right_2.frameNStart = frameN  # exact frame index
                    right_2.tStart = t  # local t and not account for scr refresh
                    right_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_2, 'tStartRefresh')  # time at next scr refresh
                    right_2.setAutoDraw(True)
                if right_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > right_2.tStartRefresh + present_time-frameTolerance:
                        # keep track of stop time/frame for later
                        right_2.tStop = t  # not accounting for scr refresh
                        right_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(right_2, 'tStopRefresh')  # time at next scr refresh
                        right_2.setAutoDraw(False)
                
                # *key_resp* updates
                waitOnFlip = False
                if key_resp.status == NOT_STARTED and tThisFlip >= start_stim_2-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp.tStartRefresh + present_time-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp.tStop = t  # not accounting for scr refresh
                        key_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                        key_resp.status = FINISHED
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                        key_resp.rt = _key_resp_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('texter.started', texter.tStartRefresh)
            trials.addData('texter.stopped', texter.tStopRefresh)
            trials.addData('cross.started', cross.tStartRefresh)
            trials.addData('cross.stopped', cross.tStopRefresh)
            trials.addData('left_star.started', left_star.tStartRefresh)
            trials.addData('left_star.stopped', left_star.tStopRefresh)
            trials.addData('right_star.started', right_star.tStartRefresh)
            trials.addData('right_star.stopped', right_star.tStopRefresh)
            trials.addData('left_2.started', left_2.tStartRefresh)
            trials.addData('left_2.stopped', left_2.tStopRefresh)
            trials.addData('right_2.started', right_2.tStartRefresh)
            trials.addData('right_2.stopped', right_2.tStopRefresh)
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
            trials.addData('key_resp.keys',key_resp.keys)
            if key_resp.keys != None:  # we had a response
                trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.started', key_resp.tStartRefresh)
            trials.addData('key_resp.stopped', key_resp.tStopRefresh)
            thisExp.addData('Rand Tim', rand_tim)
            if key_resp.keys == 'space':
                feedback = "Nice!"
            else:
                feedback = "Too Slow!"
            trial_count = trial_count +1
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "FB"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            text.setText(feedback)
            # keep track of which components have finished
            FBComponents = [text]
            for thisComponent in FBComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            FBClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "FB"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = FBClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=FBClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                        text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FBComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "FB"-------
            for thisComponent in FBComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('text.started', text.tStartRefresh)
            trials.addData('text.stopped', text.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 2 repeats of 'trials'
        
        thisExp.nextEntry()
        
    # completed 4 repeats of 'blocks'
    
    
    # ------Prepare to start Routine "end_run"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    text_6.setText(run_num)
    # keep track of which components have finished
    end_runComponents = [end, text_6, text_7]
    for thisComponent in end_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end* updates
        if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end.frameNStart = frameN  # exact frame index
            end.tStart = t  # local t and not account for scr refresh
            end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
            end.setAutoDraw(True)
        if end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                end.tStop = t  # not accounting for scr refresh
                end.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end, 'tStopRefresh')  # time at next scr refresh
                end.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_run"-------
    for thisComponent in end_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    runs.addData('end.started', end.tStartRefresh)
    runs.addData('end.stopped', end.tStopRefresh)
    rand.shuffle(arr)
    run_num = run_num+1
    block_num = -1
    runs.addData('text_6.started', text_6.tStartRefresh)
    runs.addData('text_6.stopped', text_6.tStopRefresh)
    runs.addData('text_7.started', text_7.tStartRefresh)
    runs.addData('text_7.stopped', text_7.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'runs'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
