# Spatiotemporal Attention and Decision Making

This repository contains figures and analyses from the manuscript: Linear and Nonlinear Effects of Spatial and 
Temporal Attention: Human Data and Drift Diffusion Model. 

Abstract:
Attention can be affected by expectations about where and when stimuli will appear. These two influences, spatial and temporal, 
may be present together and may interact with each other in unknown complex ways. To explore these possibilities, we used an 
attention paradigm that incorporated four variables known to produce effects on performance in a speeded reaction-time task: 
spatial cueing to indicate where a target stimulus is likely to appear, temporal statistics to indicate when the target is likely 
to appear, and preparation for a block of trials of similar length. When analyzing the data for linear trends, we found that each 
of these factors impacted performance but did not interact. When analyzing nonlinear trends in the data, we found an interaction 
between spatial and temporal attention that was modulated by preparation for a block of trials of similar length. We evaluated 
whether attentional effects across spatial, temporal, and preparatory domains could be explained by one unitary mechanism, rather 
than multiple modality-specific mechanisms, using a drift diffusion model. In the model, attention is allocated according to an 
interplay between the costs and benefits of maintaining attention. The model successfully replicated the linear effects observed 
in the human data, and accounted for some but not all nonlinear features in the data, suggesting that many disparate features of 
attention can be parsimoniously explained by a single mechanism, but some complexity in attention control remains to be 
understood. 

## Repository Structure
```text
├── data/                # Directory containing red experimental data (.csv)
├── .gitignore           # Git ignore file listing files/folders to exclude from version control
├── DDM-figures.ipynb    # Notebook for generating DDM-related figures from simulation results
├── figures.ipynb       Data visualizations in the manuscriptons (e.g., onset vs RT)
├── fit-DDM.py           # Python script to fit the DDM to behavioral data
├── run_DDM.ipynb        # Main notebook for running DDM simulations across experimental conditions
├── stats.ipynb          # Statistical analysof behavioral of results
├── README.md            # This file


