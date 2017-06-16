import logging
import threading

from constants import *
from ioutils import InputOutputOutils

class Transition:

#==============================================================================
# PUBLIC METHODS                                                             
#==============================================================================


    def __init__(self, ioutils):
        logging.debug("TRANS::Transition")        
        self.transitionToInactive()
        self.currentState = STATE_INACTIVE
        self.inputOutputUtils = ioutils

    def reset(self):
        logging.debug("TRANS::reset")
        self.transitionToInactive()
        self.currentState = STATE_INACTIVE
        self.inputOutputUtils = ioutils

    # Gets the state selected by user so the transition will be performed
    def getTransitionToPerform(self, state):
        logging.debug("TRANS::getTrans2Perform")
        self.currentState = state
        return self.inputOutputUtils.getTransitionToPerform(state)

    # Goes to innactive state
    def transitionToInactive(self):
        logging.debug("TRANS::trans2Inactive")
        
        logging.info("TRANS::transitionToIdle - Initialize mitten")
        self.inputOutputUtils.fingerControl(MITTEN, OPEN)            
            
        logging.info("TRANS::transitionToIdle - Initialize forefinger")
        self.inputOutputUtils.fingerControl(FOREFINGER, OPEN)
        
        logging.info("TRANS::transitionToIdle - Initialize thumb")
        self.inputOutputUtils.fingerControl(THUMB, OPEN)

    # Goes to idle state depending on the current one
    def transitionToIdle(self):
        logging.debug("TRANS::trans2Idle")
        threading.Thread(self.__openMitten).start()
        threading.Thread(self.__openForefinger).start()
        threading.Thread(self.__openThumb).start()
        
        
    # Goes to tongs state depending on the current one
    def transitionToTongs(self):
        logging.debug("TRANS::trans2Tongs")
        threading.Thread(self.__openMitten).start()
        threading.Thread(self.__closeForefinger).start()
        threading.Thread(self.__closeThumb).start()


    # Goes to finger state depending on the current one
    def transitionToFinger(self):
        logging.debug("TRANS::trans2Finger")
        threading.Thread(self.__closeMitten).start()
        threading.Thread(self.__openForefinger).start()
        threading.Thread(self.__closeThumb).start()


    # Goes to close state depending on the current one
    def transitionToClose(self):
        logging.debug("TRANS::trans2Close")
        threading.Thread(self.__closeMitten).start()
        threading.Thread(self.__closeForefinger).start()
        threading.Thread(self.__openThumb).start()


    # Goes to fist state depending on the current one
    def transitionToFist(self):
        logging.debug("TRANS::trans2Fist")
        threading.Thread(self.__closeMitten).start()
        threading.Thread(self.__closeForefinger).start()
        threading.Thread(self.__closeThumb).start()

    
#==============================================================================
# PRIVATE METHODS
#==============================================================================

    # Moves mitten to OPEN position if necesary
    def __openMitten(self):
        logging.debug("TRANS::openMitten")
        self.inputOutputUtils.openMitten()
  
    # Moves mitten to CLOSE postion if necesary
    def __closeMitten(self):
        logging.debug("TRANS::closeMitten")
        self.inputOutputUtils.closeMitten()

    # Moves forefinger to OPEN postion if necesary
    def __openForefinger(self):
        logging.debug("TRANS::openForefinger")
        self.inputOutputUtils.openForefinger()
        
    # Moves forefinger to CLOSE postion if necesary
    def __closeForefinger(self):
        logging.debug("TRANS::closeForefinger")
        self.inputOutputUtils.closeForefinger()

    # Moves thumb to OPEN postion if necesary
    def __openThumb(self):
        logging.debug("TRANS::openThumb")
        self.inputOutputUtils.openThumb()
        
    # Moves thumb to CLOSE postion if necesary
    def __closeThumb(self):
        logging.debug("TRANS::closeThumb")
        self.inputOutputUtils.closeThumb()

