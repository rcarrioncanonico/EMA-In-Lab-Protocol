#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on June 07, 2020, at 14:29
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'n-back-testing'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\n-back-alpha3\\nBackAlpha3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1088, 614], fullscr=True, screen=0, 
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

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='In this task you will be required to press space if the white square appeared in the same location as the location on the last trial. For example if the square was in the left down corner on trial 1 and then it appeared in the same location on trial 2, press space. Otherwise, do not respond. Press space to continue.',
    font='Arial',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp1 = keyboard.Keyboard()

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialGrid = visual.ImageStim(
    win=win,
    name='trialGrid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trialSquare = visual.Rect(
    win=win, name='trialSquare',
    width=[0.15,0.15][0], height=[0.15,0.15][1],
    ori=0.0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trialResp = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='This is the end of N-back-1 trials. You are about to start N-back-2 trials. This means that instead of pressing space whenever the square appears in the same position as on the position on one trial before, you are required to press space whenever the square appears in the same position as on the position two trials before. For example if the square appeared in left down corner on trial 1, you should press space if the square appears in the left down corner on trial 3. Press space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp2 = keyboard.Keyboard()

# Initialize components for Routine "fixation2"
fixation2Clock = core.Clock()
fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialGrid = visual.ImageStim(
    win=win,
    name='trialGrid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trialSquare = visual.Rect(
    win=win, name='trialSquare',
    width=[0.15,0.15][0], height=[0.15,0.15][1],
    ori=0.0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trialResp = keyboard.Keyboard()

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
instr3 = visual.TextStim(win=win, name='instr3',
    text='This is the end of N-back-2 trials. You are about to start N-back-3 trials. This means that instead of pressing space whenever the square appears in the same position as on the position on two trials before, you are required to press space whenever the square appears in the same position as on the position three trials before. For example if the square appeared in left down corner on trial 1, you should press space if the square appears in the left down corner on trial 4. Press space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp3 = keyboard.Keyboard()

# Initialize components for Routine "fixation3"
fixation3Clock = core.Clock()
fix3 = visual.TextStim(win=win, name='fix3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialGrid = visual.ImageStim(
    win=win,
    name='trialGrid', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
trialSquare = visual.Rect(
    win=win, name='trialSquare',
    width=[0.15,0.15][0], height=[0.15,0.15][1],
    ori=0.0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trialResp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='This is the end of the experiment.\nThank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions1"-------
continueRoutine = True
# update component parameters for each repeat
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
instructions1Components = [instr1, keyResp1]
for thisComponent in instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['space'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [fix1]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation1"-------
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBackCond1.xlsx'),
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1:
        exec('{} = thisTrials1[paramName]'.format(paramName))

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trialSquare.setPos([loc1,loc2])
    trialResp.keys = []
    trialResp.rt = []
    _trialResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trialGrid, trialSquare, trialFix, trialResp]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialGrid* updates
        if trialGrid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialGrid.frameNStart = frameN  # exact frame index
            trialGrid.tStart = t  # local t and not account for scr refresh
            trialGrid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialGrid, 'tStartRefresh')  # time at next scr refresh
            trialGrid.setAutoDraw(True)
        if trialGrid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialGrid.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trialGrid.tStop = t  # not accounting for scr refresh
                trialGrid.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialGrid, 'tStopRefresh')  # time at next scr refresh
                trialGrid.setAutoDraw(False)
        
        # *trialSquare* updates
        if trialSquare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialSquare.frameNStart = frameN  # exact frame index
            trialSquare.tStart = t  # local t and not account for scr refresh
            trialSquare.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialSquare, 'tStartRefresh')  # time at next scr refresh
            trialSquare.setAutoDraw(True)
        if trialSquare.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialSquare.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialSquare.tStop = t  # not accounting for scr refresh
                trialSquare.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialSquare, 'tStopRefresh')  # time at next scr refresh
                trialSquare.setAutoDraw(False)
        
        # *trialFix* updates
        if trialFix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix.frameNStart = frameN  # exact frame index
            trialFix.tStart = t  # local t and not account for scr refresh
            trialFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
            trialFix.setAutoDraw(True)
        if trialFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix.tStop = t  # not accounting for scr refresh
                trialFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(False)
        
        # *trialResp* updates
        waitOnFlip = False
        if trialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.tStart = t  # local t and not account for scr refresh
            trialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
            trialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialResp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trialResp.tStop = t  # not accounting for scr refresh
                trialResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialResp, 'tStopRefresh')  # time at next scr refresh
                trialResp.status = FINISHED
        if trialResp.status == STARTED and not waitOnFlip:
            theseKeys = trialResp.getKeys(keyList=['space'], waitRelease=False)
            _trialResp_allKeys.extend(theseKeys)
            if len(_trialResp_allKeys):
                trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                trialResp.rt = _trialResp_allKeys[-1].rt
                # was this correct?
                if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                    trialResp.corr = 1
                else:
                    trialResp.corr = 0
        
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
    trials1.addData('trialGrid.started', trialGrid.tStartRefresh)
    trials1.addData('trialGrid.stopped', trialGrid.tStopRefresh)
    trials1.addData('trialSquare.started', trialSquare.tStartRefresh)
    trials1.addData('trialSquare.stopped', trialSquare.tStopRefresh)
    trials1.addData('trialFix.started', trialFix.tStartRefresh)
    trials1.addData('trialFix.stopped', trialFix.tStopRefresh)
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
        trialResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp.corr = 1;  # correct non-response
        else:
           trialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials1 (TrialHandler)
    trials1.addData('trialResp.keys',trialResp.keys)
    trials1.addData('trialResp.corr', trialResp.corr)
    if trialResp.keys != None:  # we had a response
        trials1.addData('trialResp.rt', trialResp.rt)
    trials1.addData('trialResp.started', trialResp.tStartRefresh)
    trials1.addData('trialResp.stopped', trialResp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
keyResp2.keys = []
keyResp2.rt = []
_keyResp2_allKeys = []
# keep track of which components have finished
instructions2Components = [instr2, keyResp2]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        instr2.setAutoDraw(True)
    
    # *keyResp2* updates
    waitOnFlip = False
    if keyResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp2.frameNStart = frameN  # exact frame index
        keyResp2.tStart = t  # local t and not account for scr refresh
        keyResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp2, 'tStartRefresh')  # time at next scr refresh
        keyResp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp2.status == STARTED and not waitOnFlip:
        theseKeys = keyResp2.getKeys(keyList=['space'], waitRelease=False)
        _keyResp2_allKeys.extend(theseKeys)
        if len(_keyResp2_allKeys):
            keyResp2.keys = _keyResp2_allKeys[-1].name  # just the last key pressed
            keyResp2.rt = _keyResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr2.started', instr2.tStartRefresh)
thisExp.addData('instr2.stopped', instr2.tStopRefresh)
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation2Components = [fix2]
for thisComponent in fixation2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix2* updates
    if fix2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix2.frameNStart = frameN  # exact frame index
        fix2.tStart = t  # local t and not account for scr refresh
        fix2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
        fix2.setAutoDraw(True)
    if fix2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix2.tStop = t  # not accounting for scr refresh
            fix2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
            fix2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation2"-------
for thisComponent in fixation2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix2.started', fix2.tStartRefresh)
thisExp.addData('fix2.stopped', fix2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBackCond2.xlsx'),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trialSquare.setPos([loc1,loc2])
    trialResp.keys = []
    trialResp.rt = []
    _trialResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trialGrid, trialSquare, trialFix, trialResp]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialGrid* updates
        if trialGrid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialGrid.frameNStart = frameN  # exact frame index
            trialGrid.tStart = t  # local t and not account for scr refresh
            trialGrid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialGrid, 'tStartRefresh')  # time at next scr refresh
            trialGrid.setAutoDraw(True)
        if trialGrid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialGrid.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trialGrid.tStop = t  # not accounting for scr refresh
                trialGrid.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialGrid, 'tStopRefresh')  # time at next scr refresh
                trialGrid.setAutoDraw(False)
        
        # *trialSquare* updates
        if trialSquare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialSquare.frameNStart = frameN  # exact frame index
            trialSquare.tStart = t  # local t and not account for scr refresh
            trialSquare.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialSquare, 'tStartRefresh')  # time at next scr refresh
            trialSquare.setAutoDraw(True)
        if trialSquare.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialSquare.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialSquare.tStop = t  # not accounting for scr refresh
                trialSquare.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialSquare, 'tStopRefresh')  # time at next scr refresh
                trialSquare.setAutoDraw(False)
        
        # *trialFix* updates
        if trialFix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix.frameNStart = frameN  # exact frame index
            trialFix.tStart = t  # local t and not account for scr refresh
            trialFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
            trialFix.setAutoDraw(True)
        if trialFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix.tStop = t  # not accounting for scr refresh
                trialFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(False)
        
        # *trialResp* updates
        waitOnFlip = False
        if trialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.tStart = t  # local t and not account for scr refresh
            trialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
            trialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialResp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trialResp.tStop = t  # not accounting for scr refresh
                trialResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialResp, 'tStopRefresh')  # time at next scr refresh
                trialResp.status = FINISHED
        if trialResp.status == STARTED and not waitOnFlip:
            theseKeys = trialResp.getKeys(keyList=['space'], waitRelease=False)
            _trialResp_allKeys.extend(theseKeys)
            if len(_trialResp_allKeys):
                trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                trialResp.rt = _trialResp_allKeys[-1].rt
                # was this correct?
                if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                    trialResp.corr = 1
                else:
                    trialResp.corr = 0
        
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
    trials2.addData('trialGrid.started', trialGrid.tStartRefresh)
    trials2.addData('trialGrid.stopped', trialGrid.tStopRefresh)
    trials2.addData('trialSquare.started', trialSquare.tStartRefresh)
    trials2.addData('trialSquare.stopped', trialSquare.tStopRefresh)
    trials2.addData('trialFix.started', trialFix.tStartRefresh)
    trials2.addData('trialFix.stopped', trialFix.tStopRefresh)
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
        trialResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp.corr = 1;  # correct non-response
        else:
           trialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials2 (TrialHandler)
    trials2.addData('trialResp.keys',trialResp.keys)
    trials2.addData('trialResp.corr', trialResp.corr)
    if trialResp.keys != None:  # we had a response
        trials2.addData('trialResp.rt', trialResp.rt)
    trials2.addData('trialResp.started', trialResp.tStartRefresh)
    trials2.addData('trialResp.stopped', trialResp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


# ------Prepare to start Routine "instructions3"-------
continueRoutine = True
# update component parameters for each repeat
keyResp3.keys = []
keyResp3.rt = []
_keyResp3_allKeys = []
# keep track of which components have finished
instructions3Components = [instr3, keyResp3]
for thisComponent in instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr3* updates
    if instr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr3.frameNStart = frameN  # exact frame index
        instr3.tStart = t  # local t and not account for scr refresh
        instr3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr3, 'tStartRefresh')  # time at next scr refresh
        instr3.setAutoDraw(True)
    
    # *keyResp3* updates
    waitOnFlip = False
    if keyResp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp3.frameNStart = frameN  # exact frame index
        keyResp3.tStart = t  # local t and not account for scr refresh
        keyResp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp3, 'tStartRefresh')  # time at next scr refresh
        keyResp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp3.status == STARTED and not waitOnFlip:
        theseKeys = keyResp3.getKeys(keyList=['space'], waitRelease=False)
        _keyResp3_allKeys.extend(theseKeys)
        if len(_keyResp3_allKeys):
            keyResp3.keys = _keyResp3_allKeys[-1].name  # just the last key pressed
            keyResp3.rt = _keyResp3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr3.started', instr3.tStartRefresh)
thisExp.addData('instr3.stopped', instr3.tStopRefresh)
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation3"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation3Components = [fix3]
for thisComponent in fixation3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix3* updates
    if fix3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix3.frameNStart = frameN  # exact frame index
        fix3.tStart = t  # local t and not account for scr refresh
        fix3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix3, 'tStartRefresh')  # time at next scr refresh
        fix3.setAutoDraw(True)
    if fix3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix3.tStop = t  # not accounting for scr refresh
            fix3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix3, 'tStopRefresh')  # time at next scr refresh
            fix3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation3"-------
for thisComponent in fixation3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix3.started', fix3.tStartRefresh)
thisExp.addData('fix3.stopped', fix3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBackCond3.xlsx'),
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
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trialSquare.setPos([loc1,loc2])
    trialResp.keys = []
    trialResp.rt = []
    _trialResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trialGrid, trialSquare, trialFix, trialResp]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialGrid* updates
        if trialGrid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialGrid.frameNStart = frameN  # exact frame index
            trialGrid.tStart = t  # local t and not account for scr refresh
            trialGrid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialGrid, 'tStartRefresh')  # time at next scr refresh
            trialGrid.setAutoDraw(True)
        if trialGrid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialGrid.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trialGrid.tStop = t  # not accounting for scr refresh
                trialGrid.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialGrid, 'tStopRefresh')  # time at next scr refresh
                trialGrid.setAutoDraw(False)
        
        # *trialSquare* updates
        if trialSquare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialSquare.frameNStart = frameN  # exact frame index
            trialSquare.tStart = t  # local t and not account for scr refresh
            trialSquare.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialSquare, 'tStartRefresh')  # time at next scr refresh
            trialSquare.setAutoDraw(True)
        if trialSquare.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialSquare.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialSquare.tStop = t  # not accounting for scr refresh
                trialSquare.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialSquare, 'tStopRefresh')  # time at next scr refresh
                trialSquare.setAutoDraw(False)
        
        # *trialFix* updates
        if trialFix.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix.frameNStart = frameN  # exact frame index
            trialFix.tStart = t  # local t and not account for scr refresh
            trialFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
            trialFix.setAutoDraw(True)
        if trialFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix.tStop = t  # not accounting for scr refresh
                trialFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(False)
        
        # *trialResp* updates
        waitOnFlip = False
        if trialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.tStart = t  # local t and not account for scr refresh
            trialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
            trialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialResp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trialResp.tStop = t  # not accounting for scr refresh
                trialResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialResp, 'tStopRefresh')  # time at next scr refresh
                trialResp.status = FINISHED
        if trialResp.status == STARTED and not waitOnFlip:
            theseKeys = trialResp.getKeys(keyList=['space'], waitRelease=False)
            _trialResp_allKeys.extend(theseKeys)
            if len(_trialResp_allKeys):
                trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                trialResp.rt = _trialResp_allKeys[-1].rt
                # was this correct?
                if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                    trialResp.corr = 1
                else:
                    trialResp.corr = 0
        
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
    trials.addData('trialGrid.started', trialGrid.tStartRefresh)
    trials.addData('trialGrid.stopped', trialGrid.tStopRefresh)
    trials.addData('trialSquare.started', trialSquare.tStartRefresh)
    trials.addData('trialSquare.stopped', trialSquare.tStopRefresh)
    trials.addData('trialFix.started', trialFix.tStartRefresh)
    trials.addData('trialFix.stopped', trialFix.tStopRefresh)
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
        trialResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp.corr = 1;  # correct non-response
        else:
           trialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('trialResp.keys',trialResp.keys)
    trials.addData('trialResp.corr', trialResp.corr)
    if trialResp.keys != None:  # we had a response
        trials.addData('trialResp.rt', trialResp.rt)
    trials.addData('trialResp.started', trialResp.tStartRefresh)
    trials.addData('trialResp.stopped', trialResp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
