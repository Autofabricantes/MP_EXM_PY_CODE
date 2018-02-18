import logging
import time
import threading
from myoutils import Myoutils

import RPi.GPIO as GPIO

from ioutils import InputOutputOutils
from statemachine import StateMachine
from constants import *
import constants

# TODO: En el menu de pruebas meter todos los componentes a testear y que no nos embuclemos

## Autofabricantes main class
class AutofabricantesExm:
	
	## Initialization
	def __init__(self):		
		
		logging.basicConfig(level=logging.INFO, format='%(relativeCreated)6d %(threadName)s %(message)s')
				
		## counter
		self.counter  = 0
		
		## default mode
		self.mode = TEST_MODE
		self.setMode()
				
		logging.info("\n---> Setup")

		## inputOutputUtils
		self.inputOutputUtils = InputOutputOutils(self.mode)
		
		## stateMachine
		self.stateMachine = StateMachine(self.inputOutputUtils)
		self.stateMachine.start()
			
		
	## Main execution loop  
	def loop(self):
					
		while(True):
			logging.info("\n---> Loop (%i)", self.counter)
			self.counter = self.counter + 1
			self.stateMachine.executeTransition()
			
	## Reset
	def reset(self): 

		logging.debug("\n---> Reset (%i)", self.counter)		
		self.__init__()
		
 
	## setMode
	def setMode(self):
				
# 		input = GPIO.input(GPIO_INPUT_SWITCH_2)
# 		logging.info("\n---> GPIO_INPUT_SWITCH_0 [%i]", input)
# 		  
# 		if(input == 0):	
# 			## Operation mode					
# 			self.operationMode = OPERATION_MODE
# 		else:
# 			self.operationMode = TEST_MODE
		
		self.mode = TEST_MODE
		#self.mode = OPERATION_MODE
		
		logging.debug("IOUTILS::mode: %d", self.mode)

		
		
	
	
## Main execution method
def main():
	
	main = AutofabricantesExm()
	main.loop()
		

#if __name__ == "__main__": main()	
main()
