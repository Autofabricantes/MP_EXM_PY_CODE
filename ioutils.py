import logging
import time
import pid
import sys

import RPi.GPIO as GPIO
from Adafruit_MCP3008 import MCP3008
from Adafruit_PCA9685 import PCA9685

from constants import *

from test import Test
from state import State
from pid import PID

class InputOutputOutils:

#==============================================================================
# INITIALIZATION METHODS                                               
#==============================================================================

	def __init__(self):
		
		logging.debug("IOUTILS::init")
		
		# TODELETE - Test Class
		self.test = Test();		
		# State to retrieve current finger's position
		self.currentState = State();
		
		# Initialize raspberry board
		GPIO.setmode(GPIO.BCM)
		
		# Initialize input elements	 		
		GPIO.setup(GPIO_INPUT_BUTTON_0, GPIO.IN)
		GPIO.setup(GPIO_INPUT_BUTTON_1, GPIO.IN)
		GPIO.setup(GPIO_INPUT_SWITCH_0, GPIO.IN)
		GPIO.setup(GPIO_INPUT_SWITCH_1, GPIO.IN)
		GPIO.setup(GPIO_INPUT_SWITCH_2, GPIO.IN)
		GPIO.setup(GPIO_INPUT_SWITCH_3, GPIO.IN)
		
		# Initialize output elements
		GPIO.setup(GPIO_OUTPUT_LED_VBAT_OK, GPIO.OUT)		
		GPIO.setup(GPIO_OUTPUT_LED_VBAT_LOW, GPIO.OUT)
		GPIO.setup(GPIO_OUTPUT_POWER_CUT, GPIO.OUT)
		

	def setMode(self, mode):
		
		logging.debug("IOUTILS::setTestMode: %i", mode)
		self.mode = mode
		
	
	# Reset elements
	def resetElements(self):

		logging.debug("IOUTILS::resetElements")
		self.__init__()


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

		logging.debug("IOUTILS::getTransitionToPerform")

		self.currentState = state;

		if self.mode == INIT_MODE: 
			transitionTo = self.test.testInputForTransitionKeyboard()
		elif self.mode == TEST_MODE:
			transitionTo = self.test.testInputForTransitionButtons()
		else:
			transitionTo = self.geTransitionFromMyo()
			

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
	# INPUT : finger      <-- MITTEN | FOREFINGER | THUMB
	#         motorDir    <-- OPEN   | CLOSE	      
	# OUTPUT: VOID
	# TODO - TODO - While needs an output condition?
	def fingerControl(self, finger, motorDir): 
		
		logging.info("IOUTILS::fingerControl")
		
		""" With these three lines of code, the control of a single motor is achieved.
		First the feedback value of the controller is obtained from a specific channel
		of the ADC IC. Then, the control signal is computed with a PID. Finally, the
		control signal is applied to the motor as a PWM signal generated by the PWM IC.
		"""		
		# Initialize PID
		pid = PID(PID_KP, PID_KI, PID_KD)
		pid.setWindup = MOTOR_CTRL_MAX
		pid.SetPoint = 20;

		# Initialize buses
		adc = MCP3008(clk=PIN_CLK, cs=PIN_CS, miso=PIN_MISO, mosi=PIN_MOSI)

		pwm = PCA9685()
		pwm.set_pwm_freq(60)

		logging.debug("IOUTILS::fingerControl - Reading from ADC Channel [%i]", FINGER_CHANNELS_MATRIX[ADC][finger])
		logging.debug("IOUTILS::fingerControl - Reading from PWM Channel [%i]", FINGER_CHANNELS_MATRIX[PWM][finger])
					
		while True:
			feedback = adc.read_adc(FINGER_CHANNELS_MATRIX[ADC][finger])
			pid.update(feedback)
			pwm.set_pwm(FINGER_CHANNELS_MATRIX[PWM][finger], 0, pid.output)
			duty_cycle = int(input("Enter PWM duty cycle (min: -4096, max: 4096): "))
			self.motor_control(duty_cycle, finger, motorDir)			
			
		
	# TODO - TODO - Include motorDir and test
	def motor_control(self, duty_cycle, finger, motorDir):

		logging.debug("IOUTILS::motorControl - Motor Control A [%i]", FINGER_MOTORS_MATRIX[A][finger])
		logging.debug("IOUTILS::motorControl - Motor Control B [%i]", FINGER_MOTORS_MATRIX[B][finger])
	
		if(duty_cycle >= 0):
			pwm.set_pwm(FINGER_MOTORS_MATRIX[A][finger], 0, duty_cycle)		
			pwm.set_pwm(FINGER_MOTORS_MATRIX[B][finger], 0, MOTOR_CTRL_MIN)  # set pin LOW
		else:
			return
			pwm.set_pwm(FINGER_MOTORS_MATRIX[A][finger], 0, abs(duty_cycle))
			pwm.set_pwm(FINGER_MOTORS_MATRIX[B][finger], 0, MOTOR_CTRL_MAX)  # set pin HIGH
        	
        	
        	
	# Read potentiometer position
	# INPUT : finger      <-- MITTEN | FOREFINGER | THUMB
	# OUTPUT: VOID
	# TODO - TODO
	def getPotentiometerValue(self, finger):
		logging.info("IOUTILS::getPotentiometerValue")			
		return 0

	# Retrieves a transition from MYO Sensor
	# INPUT : VOID
	# OUTPUT: transition <-- TRANSITION_TO_INACTIVE | TRANSITION_TO_IDLE  | TRANSITION_TO_TONGS | 
	#                        TRANSITION_TO_FINGER   | TRANSITION_TO_CLOSE | TRANSITION_TO_FIST 
	# TODO - TODO
	def geTransitionFromMyo(self):		
		logging.info("IOUTILS::geTransitionFromMyo")
		return 0
	