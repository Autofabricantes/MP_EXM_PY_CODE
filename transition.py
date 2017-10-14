import logging
import threading

from constants import *
from ioutils import InputOutputOutils

## Transition class
class Transition:

#==============================================================================
# PUBLIC METHODS                                                             
#==============================================================================

    ## Initialization
    def __init__(self, ioutils):
        logging.debug("TRANS::Transition")        
        self.currentState = STATE_INACTIVE
        self.inputOutputUtils = ioutils
        #self.transitionToInactive()

    ## Reset
    def reset(self):
        logging.debug("TRANS::reset")
        self.currentState = STATE_INACTIVE
        self.inputOutputUtils = ioutils
        #self.transitionToInactive()

    ## Gets the state selected by user so the transition will be performed
    # @param state
    def getTransitionToPerform(self, state):
        logging.debug("TRANS::getTrans2Perform")
        self.currentState = state
        return self.inputOutputUtils.getTransitionToPerform(state)

    ## Goes to innactive state
    def transitionToInactive(self):
        logging.debug("TRANS::trans2Inactive")
        
        logging.info("TRANS::transitionToIdle - Initialize mitten")
        self.inputOutputUtils.fingerControl(MITTEN, OPEN)            
            
        logging.info("TRANS::transitionToIdle - Initialize forefinger")
        self.inputOutputUtils.fingerControl(FOREFINGER, OPEN)
        
        logging.info("TRANS::transitionToIdle - Initialize thumb")
        self.inputOutputUtils.fingerControl(THUMB, OPEN)

    ## Goes to idle state depending on the current one
    def transitionToIdle(self):
        
        logging.debug("TRANS::trans2Idle")
        
        threadMitten = threading.Thread(target=self.__openMitten, name="Thread-Open-Mitten")
        threadForefinger = threading.Thread(target=self.__openForefinger, name="Thread-Open-Forefinger")
        threadThumb = threading.Thread(target=self.__openThumb, name="Thread-Open-Thumb")
        
        threadMitten.start()
        threadForefinger.start()
        threadThumb.start()
        
        threadMitten.join()
        threadForefinger.join()
        threadThumb.join()
        
    ## Goes to tongs state depending on the current one
    def transitionToTongs(self):
        
        logging.debug("TRANS::trans2Tongs")
        
        threadMitten = threading.Thread(target=self.__openMitten, name="Thread-OPen-Mitten")
        threadForefinger = threading.Thread(target=self.__closeForefinger, name="Thread-Close-Forefinger")
        threadThumb = threading.Thread(target=self.__closeThumb, name="Thread-Close-Thumb")
        
        threadMitten.start()
        threadForefinger.start()
        threadThumb.start()
        
        threadMitten.join()
        threadForefinger.join()
        threadThumb.join()


    ## Goes to finger state depending on the current one
    def transitionToFinger(self):
        
        logging.debug("TRANS::trans2Finger")
        
        threadMitten = threading.Thread(target=self.__closeMitten, name="Thread-Close-Mitten")
        threadForefinger = threading.Thread(target=self.__openForefinger, name="Thread-Open-Forefinger")
        threadThumb = threading.Thread(target=self.__closeThumb, name="Thread-Close-Thumb")
        
        threadMitten.start()
        threadForefinger.start()
        threadThumb.start()
        
        threadMitten.join()
        threadForefinger.join()
        threadThumb.join()


    ## Goes to close state depending on the current one
    def transitionToClose(self):
        
        logging.debug("TRANS::trans2Close")
        
        threadMitten = threading.Thread(target=self.__closeMitten, name="Thread-Close-Mitten")
        threadForefinger = threading.Thread(target=self.__closeForefinger, name="Thread-Close-Forefinger")
        threadThumb = threading.Thread(target=self.__openThumb, name="Thread-Open-Thumb")
        
        threadMitten.start()
        threadForefinger.start()
        threadThumb.start()
        
        threadMitten.join()
        threadForefinger.join()
        threadThumb.join()


    ## Goes to fist state depending on the current one
    def transitionToFist(self):
        
        logging.debug("TRANS::trans2Fist")
        
        threadMitten = threading.Thread(target=self.__closeMitten, name="Thread-Close-Mitten")
        threadForefinger = threading.Thread(target=self.__closeForefinger, name="Thread-Close-Forefinger")
        threadThumb = threading.Thread(target=self.__closeThumb, name="Thread-Close-Thumb")
        
        threadMitten.start()
        threadForefinger.start()
        threadThumb.start()
        
        threadMitten.join()
        threadForefinger.join()
        threadThumb.join()

    
#==============================================================================
# PRIVATE METHODS
#==============================================================================

    ## Moves mitten to OPEN position if necesary
    def __openMitten(self):
        logging.debug("TRANS::openMitten")
        self.inputOutputUtils.openMitten()
  
    ## Moves mitten to CLOSE postion if necesary
    def __closeMitten(self):
        logging.debug("TRANS::closeMitten")
        self.inputOutputUtils.closeMitten()

    ## Moves forefinger to OPEN postion if necesary
    def __openForefinger(self):
        logging.debug("TRANS::openForefinger")
        self.inputOutputUtils.openForefinger()
        
    ## Moves forefinger to CLOSE postion if necesary
    def __closeForefinger(self):
        logging.debug("TRANS::closeForefinger")
        self.inputOutputUtils.closeForefinger()

    ## Moves thumb to OPEN postion if necesary
    def __openThumb(self):
        logging.debug("TRANS::openThumb")
        self.inputOutputUtils.openThumb()
        
    ## Moves thumb to CLOSE postion if necesary
    def __closeThumb(self):
        logging.debug("TRANS::closeThumb")
        self.inputOutputUtils.closeThumb()

