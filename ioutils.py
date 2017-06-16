import logging
import time
import pid
import sys

import RPi.GPIO as GPIO
from numpy import interp

from constants import *

from test import Test
from state import State
from pid import PID

class InputOutputOutils:

#==============================================================================
# INITIALIZATION INPUT METHODS                                               
#==============================================================================

	def __init__(self):
		
		# TODELETE - Test Class
		self.test = Test();		
		# State to retrieve current finger's position
		self.currentState = State();
		# Initialize raspberry board
		# GPIO.setmode(GPIO.BOARD)	
		GPIO.setmode(GPIO.BCM)
			

	# Initialization of INPUT sensors
	def initializeInputElements(self): 

		logging.debug("IOUTILS::initInput")
		
		GPIO.setup(PIN_INPUT_BUTTON_0, GPIO.IN)
		GPIO.setup(PIN_INPUT_BUTTON_1, GPIO.IN)
		GPIO.setup(PIN_INPUT_SWITCH_0, GPIO.IN)
		GPIO.setup(PIN_INPUT_SWITCH_1, GPIO.IN)
		GPIO.setup(PIN_INPUT_SWITCH_2, GPIO.IN)
		GPIO.setup(PIN_INPUT_SWITCH_3, GPIO.IN)
		


	# Reset of INPUT sensors
	def resetInputElements(self): 

		logging.debug("IOUTILS::resetInput")
		self.initializeInputElements()



#==============================================================================
# INITIALIZATION OUTPUT METHODS                                              
#==============================================================================

	# Initialization of OUTPUT elements
	def initializeOutputElements(self):

		logging.info("IOUTILS::initOutput")
		
		GPIO.setup(PIN_OUTPUT_LED_VBAT_OK, GPIO.OUT)
		GPIO.setup(PIN_OUTPUT_LED_VBAT_LOW, GPIO.OUT)
		GPIO.setup(PIN_OUTPUT_POWER_CUT, GPIO.OUT)		
		
		
	# Reset of OUTPUT elements
	def resetOutputElements(self):

		logging.debug("IOUTILS::resetOutput")
		self.initializeOutputElements()



#==============================================================================
# FINGERS POSITION                                                           
#==============================================================================

	# Detects mitten position from output elements feedback
	# returns: OPEN|CLOSE
	# TODO: Two solutions for fingers position
	#  - Detect where the finger is
	#  - Trust where the state says we are
	def getMittenPosition(self):

		# TODO: What happens if finger position is diferent to current position?
		# Tenedremos que revisar en que posicion se encuentar el dedo realmente para
		# restaurar la posicion si es necesario.
		mittenPosition = self.currentState.getMittenPosition()

		logging.info("IOUTILS::getMittenPos: %i", mittenPosition)

		return mittenPosition;

	# Detects forefinger position from output elements feedback
	# returns: OPEN|CLOSE
	# TODO: Two solutions for fingers position
	#  - Detect where the finger is
	#  - Trust where the state says we are
	def getForefingerPosition(self):

		# TODO: What happens if finger position is diferent to current position?
		# Tenedremos que revisar en que posicion se encuentar el dedo realmente para
		# restaurar la posicion si es necesario.
		forefingerPosition = self.currentState.getForefingerPosition()

		logging.debug("IOUTILS::getForefingerPos: %i", forefingerPosition)

		return forefingerPosition

	# Detects thumb position from output elements feedback
	# returns: OPEN|CLOSE
	# TODO: Two solutions for fingers position
	#  - Detect where the finger is
	#  - Trust where the state says we are
	def getThumbPosition(self):

		# TODO: What happens if finger position is diferent to current position?
		# Tenedremos que revisar en que posicion se encuentar el dedo realmente para
		# restaurar la posicion si es necesario.
		thumbPosition = self.currentState.getThumbPosition()

		logging.debug("getThumbPos: %i", thumbPosition)

		return thumbPosition



#==============================================================================
# TRANSITIONS                                                                
#==============================================================================

	# Identifies the state selected by user from input elements feedback
	# An interpretation and treatment of readed data from sensors will be  
	# needed to perform the required transition to get the selected state 
	# without  ambiguity
	# returns: Transition value
	def getTransitionToPerform(self, state): 

		logging.debug("IOUTILS::getTrans")

		self.currentState = state;

		# Test Menu
		#transitionTo = self.test.testInputForTransitionButtons()
		#transitionTo = self.geTransitionFromMyo() 
		transitionTo = self.test.testInputForTransitionKeyboard()

		return transitionTo

	# Moves mitten to OPEN position if necessary
	def openMitten(self): 

		logging.debug("IOUTILS::openMitten")

		if(self.getMittenPosition() == CLOSE):
			logging.info("IOUTILS::openMitten-OPEN")
			self.fingerControl(MITTEN, OPEN)
							
	# Moves mitten to CLOSE position if necessary
	def closeMitten(self):

		logging.debug("IOUTILS::closeMitten")

		if(self.getMittenPosition() == OPEN):
			logging.info("IOUTILS::closeMitten - CLOSE");
			self.fingerControl(MITTEN, CLOSE)
	
	# Moves forefinger to OPEN position if necessary
	def openForefinger(self): 

		logging.debug("IOUTILS::openForefinger")

		if(self.getForefingerPosition() == CLOSE):
			logging.debug("IOUTILS::openForefinger - OPEN")
			self.fingerControl(FOREFINGER, OPEN)
			
	# Moves forefinger to CLOSE position if necessary
	def closeForefinger(self):

		logging.debug("IOUTILS::closeForefinger")

		if(self.getForefingerPosition() == OPEN):
			logging.debug("IOUTILS::closeForefinger - CLOSE")
			self.fingerControl(FOREFINGER, CLOSE)
			
	# Moves thumb to OPEN position if necessary
	def openThumb(self):

		logging.debug("IOUTILS::openThumb");

		if(self.getThumbPosition() == CLOSE):
			logging.debug("IOUTILS::openThumb - OPEN")
			self.fingerControl(THUMB, OPEN)
	
	# Moves mitten to CLOSE position if necessary
	def closeThumb(self):

		logging.debug("IOUTILS::closeThumb")

		if(self.getThumbPosition() == CLOSE):
			logging.debug("IOUTILS::closeThumb - CLOSE")
			self.fingerControl(THUMB, CLOSE)


#==============================================================================
# PCB CONTROLS                                                               
#==============================================================================

	# Finger control method
	def fingerControl(self, finger, motorDir):
		
		logging.info("IOUTILS::fingerControl")		
		
		input = interp(self.getPotentiometerValue(finger), [0, 1023], [MOTOR_SPEED_MIN, MOTOR_SPEED])		
					   	
		logging.info("IOUTILS::fingerControl - input: %f", input)
		
		#output = sys.maxsize
		output = 0
		
		if motorDir == OPEN:
			setpoint = MOTOR_SPEED_MIN
			direction =  pid.REVERSE			
			logging.info("IOUTILS::fingerControl - OPEN - final setpoint: %f", setpoint)	    	   	    	    					
		else:
			setpoint = MOTOR_SPEED
			direction =  pid.DIRECT
			logging.info("IOUTILS::fingerControl - CLOSE - final setpoint: %f", setpoint)
			  
		# Initialize PID
		myPid = PID(input, output, setpoint, pid.PID_KP, pid.PID_KI, pid.PID_KD, direction)
    	 	    	 			
    	# Turn on the PID loop
		# myPid.set_mode(AUTOMATIC)
		myPid.set_output_limits(0, MOTOR_SPEED)
		
		while(abs(input - setpoint) >  pid.PID_LIMITS):
			
			input = interp(self.getPotentiometerValue(finger),[0,1023],[MOTOR_SPEED_MIN, MOTOR_SPEED])
			
			myPid.compute();
			
			logging.info("IOUTILS::fingerControl - input: %f", input)
			logging.info("IOUTILS::fingerControl - setpoint: %f", setpoint)  
			logging.info("IOUTILS::fingerControl - output: %f", output)
     		
			self.motorControl(finger, motorDir, round(output))
			
						
		logging.info("IOUTILS::fingerControl - Stopping motor")			
		self.motorControl(finger, motorDir, MOTOR_SPEED_MIN)


	# Motor Control method
	# INPUT : finger      <-- MITTEN | FOREFINGER | THUMB
	#         motorDir    <-- OPEN   | CLOSE
	#         motorSpeed  <-- MOTOR_SPEED_MIN  | MOTOR_SPEED  | MOTOR_SPEED_MAX       
	# OUTPUT: VOID
	def motorControl(self, finger, motorDir, motorSpeed): 
		logging.info("IOUTILS::motorControl")
		return 0
	

	# Read potentiometer position
	# INPUT : finger      <-- MITTEN | FOREFINGER | THUMB
	# OUTPUT: VOID
	def getPotentiometerValue(self, finger):
		logging.info("IOUTILS::getPotentiometerValue")
		return 0

	# Retrieves a transition from MYO Sensor
	# INPUT : VOID
	# OUTPUT: transition <-- TRANSITION_TO_INACTIVE | TRANSITION_TO_IDLE  | TRANSITION_TO_TONGS | 
	#                        TRANSITION_TO_FINGER   | TRANSITION_TO_CLOSE | TRANSITION_TO_FIST 
	def geTransitionFromMyo(self):		
		logging.info("IOUTILS::geTransitionFromMyo")
		return 0
	