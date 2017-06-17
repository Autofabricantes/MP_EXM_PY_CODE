import logging
import time

import RPi.GPIO as GPIO

from ioutils import InputOutputOutils
from statemachine import StateMachine
from constants import *
import constants

class AutofabricantesExm:
    
    def __init__(self):        
        
        logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
        
        self.counter  = 0;
        self.testMode = False
                    
        logging.info("\n---> Setup")

        self.inputOutputUtils = InputOutputOutils()
        self.inputOutputUtils.initializeInputElements()
        self.inputOutputUtils.initializeOutputElements()
        
        self.stateMachine = StateMachine(self.inputOutputUtils)
        self.stateMachine.start()
                     
        self.mode = self.setMode()  
        
      
    def loop(self):
                    
        while(True):
            logging.info("\n---> Loop (%i)", self.counter)
            self.counter = self.counter + 1
            self.stateMachine.executeTransition()
            

    def reset(self): 

        logging.debug("\n---> Reset (%i)", self.counter)
           
        self.inputOutputUtils.initializeInputElements()

        self.inputOutputUtils.initializeOutputElements()

        self.stateMachine.reset();
 
    # TODO - Read from switches and depending on the one is active,the operation mode is set
    # Now, only SWITCH_1 is working
    def setMode(self):
                
        input = GPIO.input(PIN_INPUT_SWITCH_2)
        logging.info("\n---> PIN_INPUT_SWITCH_0 [%i]", input)
          
        if(input == 0):                        
            self.operationMode = INIT_MODE
        else:
            self.operationMode = TEST_MODE
            
        self.inputOutputUtils.setMode(self.operationMode)
        

def main():
    
    main = AutofabricantesExm()
    main.loop()
        
    
main()

    
