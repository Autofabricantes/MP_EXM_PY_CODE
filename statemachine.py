import logging
import constants

from state import State
from transition import Transition
from test import Test

class StateMachine: 

#==============================================================================
# PUBLIC METHODS                                                             
#==============================================================================

    def __init__(self):
        
        # State machine's state
        self.state = State()
        # State machine's transition
        self.transition = Transition()
        # test class to handle LEDs colors depending on current state
        self.test = Test()


    # Starts state machine
    def start(self):

        logging.debug("STM::start")

        self.state.setCurrentState(constants.TRANSITION_TO_INACTIVE);
        self.test.testInitializeLedStripe();
        
  
    # Resets state machine
    def reset(self):

        logging.debug("STM::reset")

        self.state.reset();
        self.transition.reset();
        self.test.testInitializeLedStripe();        
        

    # Execute a transition
    def executeTransition(self):

        logging.debug("STM::executeTrans")
    
        currentState = self.state.getCurrentState();

        transitionToPeform = self.transition.getTransitionToPerform(self.state)

        logging.debug("STM::executeTrans: %i", transitionToPeform)
        
        if(transitionToPeform == constants.TRANSITION_TO_INACTIVE):
            self.transition.transitionToInactive()
            self.test.testOutputWithLedStripe(0,0,0,0)
            self.state.setCurrentState(constants.STATE_INACTIVE)
                
        elif(transitionToPeform == constants.TRANSITION_TO_IDLE):
            self.transition.transitionToIdle()
            self.test.testOutputWithLedStripe(0,102,204,0)
            self.state.setCurrentState(constants.STATE_IDLE)
        
        elif(transitionToPeform == constants.TRANSITION_TO_TONGS):
            if(currentState != constants.STATE_INACTIVE):
                self.transition.transitionToTongs()
                self.test.testOutputWithLedStripe(0,0,128,255)
                self.state.setCurrentState(constants.STATE_TONGS)

        elif(transitionToPeform == constants.TRANSITION_TO_FINGER):            
            if(currentState != constants.STATE_INACTIVE):
                self.transition.transitionToFinger()
                self.test.testOutputWithLedStripe(0,255,255,0)
                self.state.setCurrentState(constants.STATE_FINGER)        
        
        elif(transitionToPeform == constants.TRANSITION_TO_CLOSE):                
            if(currentState != constants.STATE_INACTIVE):
                self.transition.transitionToClose()
                self.test.testOutputWithLedStripe(0,153,0,153)
                self.state.setCurrentState(constants.STATE_CLOSE)        
            
        elif(transitionToPeform == constants.TRANSITION_TO_FIST):        
            if(currentState != constants.STATE_INACTIVE):
                self.transition.transitionToFist()
                self.test.testOutputWithLedStripe(0,204,0,0)
                self.state.setCurrentState(constants.STATE_FIST)

        else:
            
            logging.debug("STM::executeTrans - Invalid transition: %i", self.transitionToPeform)


