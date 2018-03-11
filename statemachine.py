import logging
import time

from state import State
from transition import Transition
from test import Test
from constants import *

import ioutils

## State machine class
class StateMachine: 

#==============================================================================
# PUBLIC METHODS                                                             
#==============================================================================

    ## Initialization
    def __init__(self, ioutils):
        
        # State machine's state
        self.state = State()
        # State machine's transition
        self.transition = Transition(ioutils)
        # test class to handle LEDs colors depending on current state
        self.test = Test()


    ## Starts state machine
    def start(self):

        logging.debug("STM::start")

        self.state.setCurrentState(TRANSITION_TO_INACTIVE);
        
  
    ## Resets state machine
    def reset(self):

        logging.debug("STM::reset")

        self.state.reset();
        self.transition.reset();
        
        

    ## Execute a transition
    def executeTransition(self):

        logging.debug("STM::executeTransition")
    
        currentState = self.state.getCurrentState();

        transitionToPeform = self.transition.getTransitionToPerform(self.state)

        logging.debug("STM::executeTransition: %i", transitionToPeform)
        
        if(transitionToPeform == TRANSITION_TO_INACTIVE):
            self.transition.transitionToInactive()            
            self.state.setCurrentState(STATE_INACTIVE)
                
        elif(transitionToPeform == TRANSITION_TO_IDLE):
            self.transition.transitionToIdle()            
            self.state.setCurrentState(STATE_IDLE)
            logging.info("STM::Waiting to finish transition")
            time.sleep(5)
        
        elif(transitionToPeform == TRANSITION_TO_TONGS):
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToTongs()                
                self.state.setCurrentState(STATE_TONGS)
                logging.info("STM::Waiting to finish transition")
                time.sleep(5)

        elif(transitionToPeform == TRANSITION_TO_FINGER):            
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToFinger()                
                self.state.setCurrentState(STATE_FINGER)
                logging.info("STM::Waiting to finish transition")
                time.sleep(5)        
        
        elif(transitionToPeform == TRANSITION_TO_CLOSE):                
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToClose()                
                self.state.setCurrentState(STATE_CLOSE)
                logging.info("STM::Waiting to finish transition")
                time.sleep(5)        
            
        elif(transitionToPeform == TRANSITION_TO_FIST):        
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToFist()
                self.state.setCurrentState(STATE_FIST)
                logging.info("STM::waiting to finish transition")
                time.sleep(5)

        elif(transitionToPeform == TRANSITION_TO_NOTHING):
            logging.debug("STM::executeTransition - Nothing to do")       
                 
        else:
            logging.debug("STM::executeTransition - Invalid transition: %i", transitionToPeform)
                   

    ## Getter
    def getTransition(self):
        return self.transition;
