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
        self.test.testInitializeLedStripe();
        
  
    ## Resets state machine
    def reset(self):

        logging.debug("STM::reset")

        self.state.reset();
        self.transition.reset();
        self.test.testInitializeLedStripe();        
        

    ## Execute a transition
    def executeTransition(self):

        logging.debug("STM::executeTransition")
    
        currentState = self.state.getCurrentState();

        transitionToPeform = self.transition.getTransitionToPerform(self.state)

        logging.info("STM::executeTransition: %i", transitionToPeform)
        
        if(transitionToPeform == TRANSITION_TO_INACTIVE):
            self.transition.transitionToInactive()
            self.test.testOutputWithLedStripe(0,0,0,0)
            self.state.setCurrentState(STATE_INACTIVE)
                
        elif(transitionToPeform == TRANSITION_TO_IDLE):
            self.transition.transitionToIdle()
            self.test.testOutputWithLedStripe(0,102,204,0)
            self.state.setCurrentState(STATE_IDLE)
        
        elif(transitionToPeform == TRANSITION_TO_TONGS):
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToTongs()
                self.test.testOutputWithLedStripe(0,0,128,255)
                self.state.setCurrentState(STATE_TONGS)

        elif(transitionToPeform == TRANSITION_TO_FINGER):            
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToFinger()
                self.test.testOutputWithLedStripe(0,255,255,0)
                self.state.setCurrentState(STATE_FINGER)        
        
        elif(transitionToPeform == TRANSITION_TO_CLOSE):                
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToClose()
                self.test.testOutputWithLedStripe(0,153,0,153)
                self.state.setCurrentState(STATE_CLOSE)        
            
        elif(transitionToPeform == TRANSITION_TO_FIST):        
            if(currentState != STATE_INACTIVE):
                self.transition.transitionToFist()
                self.test.testOutputWithLedStripe(0,204,0,0)
                self.state.setCurrentState(STATE_FIST)

        else:
            
            logging.debug("STM::executeTransition - Invalid transition: %i", transitionToPeform)
            
       
        logging.info("STM::waiting to finish transition")
        time.sleep(5)

            

    ## Getter
    def getTransition(self):
        return self.transition;
