import logging

from ioutils import InputOutputOutils

class Transition:

#==============================================================================
# PUBLIC METHODS                                                             
#==============================================================================

    def __init__(self):
        logging.debug("TRANS::Transition")
        self.currentState = constants.STATE_INACTIVE
        self.inputOutputUtils = InputOutputOutils()

    def reset(self):
        logging.debug("TRANS::reset")
        self.transitionToInactive()

    def getTransitionToPerform(self, state):
        logging.debug("TRANS::getTrans2Perform")
        self.currentState = state
        return self.inputOutputUtils.getTransitionToPerform(state)

    def transitionToInactive(self):
        logging.debug("TRANS::trans2Inactive")
        self.__openMitten()
        self.__openForefinger()
        self.__openThumb()

    def transitionToIdle(self):
        logging.debug("TRANS::trans2Idle")
        
        if(self.currentState == constants.STATE_INACTIVE):
            logging.debug("TRANS::trans2Inactive")
            self.__openMitten()
            self.__openForefinger()
            self.__openThumb()
        else:
            logging.info("TRANS::transitionToIdle - Initialize mitten")
            self.initialFingerControl(constants.MITTEN, constants.CONTROL_INPUT_POTENTIOMETER_MITTEN)			
            
            logging.info("TRANS::transitionToIdle - Initialize forefinger")
            self.initialFingerControl(constants.FOREFINGER, constants.CONTROL_INPUT_POTENTIOMETER_FOREFINGER)
			
            logging.info("TRANS::transitionToIdle - Initialize thumb")
            self.initialFingerControl(constants.THUMB, constants.CONTROL_INPUT_POTENTIOMETER_THUMB)
			

    def transitionToTongs(self):
        logging.debug("TRANS::trans2Tongs")
        self.__openMitten()
        self.__closeForefinger()
        self.__closeThumb()

    def transitionToFinger(self):
        logging.debug("TRANS::trans2Finger")
        self.__closeMitten()
        self.__openForefinger()
        self.__closeThumb()

    def transitionToClose(self):
        logging.debug("TRANS::trans2Close")
        self.__closeMitten()
        self.__closeForefinger()
        self.__openThumb()

    def transitionToFist(self):
        logging.debug("TRANS::trans2Fist")
        self.__closeMitten()
        self.__closeForefinger()
        self.__closeThumb()

    
#==============================================================================
# PRIVATE METHODS
#==============================================================================

    def __openMitten(self):
        logging.debug("TRANS::openMitten")
        self.inputOutputUtils.openMitten()
  
    def __closeMitten(self):
        logging.debug("TRANS::closeMitten")
        self.inputOutputUtils.closeMitten()

    def __openForefinger(self):
        logging.debug("TRANS::openForefinger")
        self.inputOutputUtils.openForefinger()

    def __closeForefinger(self):
        logging.debug("TRANS::closeForefinger")
        self.inputOutputUtils.closeForefinger()

    def __openThumb(self):
        logging.debug("TRANS::openThumb")
        self.inputOutputUtils.openThumb()
        
    def __closeThumb(self):
        logging.debug("TRANS::closeThumb")
        self.inputOutputUtils.closeThumb()

