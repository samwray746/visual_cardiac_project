# This is the main script for a task in which Gabor patches are presented at systole/diastole. Some details: 
# - A fixation dot is presented centrally on the screen throughout the task (0.2 degree size)
# - During each trial, a Gabor patch (2 degree size) is presented at a 4 degree eccentricity from the fixation dot 
# - The Gabor patch can either be high-frequency (6 cpd) or low-frequency (3 cpd) 
# - During each trial, the Gabor patch will be presented after an R-peak sensing period at systole/diastole for 40ms 
# - After Gabor-patch presentation there will be an ISI of 2-3 seconds
# - When the fixation dot turns yellow, participants respond according to whether the Gabor patch was tilted clockwise or counterclockwise (1.5s)
# - Then, another inter-trial interval of 2-3 seconds 
# - In total, there are 3 blocks of 60 trials. Each block will have 15 HF-S/LF-S/HF-D/LF-D

import psychopy
import os.path as op
from psychopy import event, visual, gui, core
from statistics import mean

from intart_functions import sendParallelTrigger, readParallelTrigger
from create_stimuli_function import create_experimental_stimuli
from experiment_variables_function import experiment_variables
from save_file_modification_function import save_file_modification
from instructions_function import instructions
from experiment_block_function import experiment_block 
from save_experimental_block_function import save_experimental_block

### GATHERING PARTICIPANT INFO ### 

participant_info = {'Subject ID': '', 'Age': '', 'Sex': ['M', 'F'],
                    'Order, frequency': '', 'Order, phase': '', 'Random seed': ''}

# The two orders refer to the two variables of high- and low-frequency, and systole and diastole

myDlg = gui.DlgFromDict(participant_info, title="Sam gaze experiment")

if not myDlg.OK:
    core.quit()
    
order = int(participant_info['Order']) # this is for the order in which systole/diastole blocks are presented (two possible orders, 1 and 2)
subject_id = str(participant_info['Subject ID'])
random_seed = int(participant_info['Random seed'])
age = str(participant_info['Age'])
sex = str(participant_info['Sex'])
counterbalance_group = int(participant_info['Counterbalance group']) # and this is for the order in which the faces are presented (6 possible groups) 

win = visual.Window(color = '#000000', fullscr = True, monitor="testMonitor", units="pix")
win.mouseVisible = False








