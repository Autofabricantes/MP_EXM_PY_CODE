import logging
import time
import pid
import sys

import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

from Adafruit_MCP3008 import MCP3008
from Adafruit_PCA9685 import PCA9685  

from constants import *

from test import Test
from state import State
from pid import PID
from myoutils import Myoutils

## Software communication with sensors
class InputOutputOutils:

#==============================================================================
# INITIALIZATION METHODS											   
#==============================================================================

	## Initialization 
	def __init__(self, mode):		
		
		logging.debug("IOUTILS::init")

		# Setting mode
		self.mode = mode
				
		## State to retrieve current finger's position
		self.currentState = State();		
		      
		## init MYO
		self.myo = Myoutils(mode)

		if(self.mode == OPERATION_MODE):
			self.myo.startThreadMyo()
          
		## Test helper class attribute
		self.test = Test(self.myo);		
		
		# Initialize raspberry board
		GPIO.setmode(GPIO.BCM)
		
		# Initialize input elements	 		
		#GPIO.setup(GPIO_INPUT_BUTTON_0, GPIO.IN)
		#GPIO.setup(GPIO_INPUT_BUTTON_1, GPIO.IN)
		#GPIO.setup(GPIO_INPUT_SWITCH_0, GPIO.IN)
		#GPIO.setup(GPIO_INPUT_SWITCH_1, GPIO.IN)
		#GPIO.setup(GPIO_INPUT_SWITCH_2, GPIO.IN)
		#GPIO.setup(GPIO_INPUT_SWITCH_3, GPIO.IN)
		
		# Initialize output elements
		GPIO.setup(GPIO_OUTPUT_LED_VBAT_OK, GPIO.OUT)		
		GPIO.setup(GPIO_OUTPUT_LED_VBAT_LOW, GPIO.OUT)
		GPIO.setup(GPIO_OUTPUT_POWER_CUT, GPIO.OUT)
		
		GPIO.setup(MOT_0_A_CTRL, GPIO.OUT)
		GPIO.setup(MOT_0_B_CTRL, GPIO.OUT)
		GPIO.setup(MOT_1_A_CTRL, GPIO.OUT)
		GPIO.setup(MOT_1_B_CTRL, GPIO.OUT)
		GPIO.setup(MOT_2_A_CTRL, GPIO.OUT)
		GPIO.setup(MOT_2_B_CTRL, GPIO.OUT)
		
		# Initialize PWM
		# TODO - Here or in fingerControl?
		self.pwm = PCA9685.PCA9685(PCA_I2C_ADDR)
		self.pwm.set_pwm_freq(PWM_FRQUENCY)
		
		#initialize ADC
		# TODO - Here or in fingerControl?
		self.adc = MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

		
	## Reset elements
	def resetElements(self):
		
		logging.debug("IOUTILS::resetElements")
		self.__init__()


#==============================================================================
# FINGERS POSITION														   
#==============================================================================

	## Detects mitten position from output elements feedback
	#  @param self
	#  @return OPEN|CLOSE
	def getMittenPosition(self):
		
		# TODO: Two solutions for fingers position
		#	 - Detect where the finger is
		#	 - Trust where the state says we are		
		# TODO: What happens if finger position is diferent to current position?
		# Tenedremos que revisar en que posicion se encuentar el dedo realmente para
		# restaurar la posicion si es necesario.
		mittenPosition = self.currentState.getMittenPosition()

		logging.info("IOUTILS::getMittenPos: %i", mittenPosition)

		return mittenPosition

	
	## Detects forefinger position from output elements feedback
	#  @return OPEN|CLOSE
	def getForefingerPosition(self):
		
		# TODO: Two solutions for fingers position
		#  - Detect where the finger is
		#  - Trust where the state says we are
	
		
		# TODO: What happens if finger position is diferent to current position?
		# Tenedremos que revisar en que posicion se encuentar el dedo realmente para
		# restaurar la posicion si es necesario.
		forefingerPosition = self.currentState.getForefingerPosition()

		logging.debug("IOUTILS::getForefingerPos: %i", forefingerPosition)

		return forefingerPosition
	
	## Detects thumb position from output elements feedback
	#  @return  OPEN|CLOSE
	def getThumbPosition(self):

		# TODO: Two solutions for fingers position
		#  - Detect where the finger is
		#  - Trust where the state says we are
		# TODO: What happens if finger position is diferent to current position?
		# Tenedremos que revisar en que posicion se encuentar el dedo realmente para
		# restaurar la posicion si es necesario.
		thumbPosition = self.currentState.getThumbPosition()

		logging.debug("getThumbPos: %i", thumbPosition)

		return thumbPosition


#==============================================================================
# TRANSITIONS																
#==============================================================================

	## Identifies the state selected by user from input elements feedback
	#  An interpretation and treatment of readed data from sensors will be  
	#  needed to perform the required transition to get the selected state 
	#  without  ambiguity
	#  @return Transition value
	def getTransitionToPerform(self, state): 

		logging.debug("IOUTILS::getTransitionToPerform")

		self.currentState = state;

		if self.mode == TEST_MODE:
			transitionTo = self.test.testInputForTransitionKeyboard()
		else:
			transitionTo = self.geTransitionFromMyo()
			

		return transitionTo

	## Moves mitten to OPEN position if necessary
	def openMitten(self): 

		logging.debug("IOUTILS::openMitten")

		if(self.getMittenPosition() == CLOSE):
			logging.info("IOUTILS::openMitten-OPEN")
			self.fingerControl(MITTEN, OPEN)
							
	## Moves mitten to CLOSE position if necessary
	def closeMitten(self):

		logging.debug("IOUTILS::closeMitten")

		if(self.getMittenPosition() == OPEN):
			logging.info("IOUTILS::closeMitten - CLOSE");
			self.fingerControl(MITTEN, CLOSE)
	
	## Moves forefinger to OPEN position if necessary
	def openForefinger(self): 

		logging.debug("IOUTILS::openForefinger")

		if(self.getForefingerPosition() == CLOSE):
			logging.debug("IOUTILS::openForefinger - OPEN")
			self.fingerControl(FOREFINGER, OPEN)
			
	## Moves forefinger to CLOSE position if necessary
	def closeForefinger(self):

		logging.debug("IOUTILS::closeForefinger")

		if(self.getForefingerPosition() == OPEN):
			logging.debug("IOUTILS::closeForefinger - CLOSE")
			self.fingerControl(FOREFINGER, CLOSE)
			
	## Moves thumb to OPEN position if necessary
	def openThumb(self):

		logging.debug("IOUTILS::openThumb");

		if(self.getThumbPosition() == CLOSE):
			logging.debug("IOUTILS::openThumb - OPEN")
			self.fingerControl(THUMB, OPEN)
	
	## Moves mitten to CLOSE position if necessary
	def closeThumb(self):

		logging.debug("IOUTILS::closeThumb")

		if(self.getThumbPosition() == CLOSE):
			logging.debug("IOUTILS::closeThumb - CLOSE")
			self.fingerControl(THUMB, CLOSE)

		

#==============================================================================
# PCB CONTROLS															   
#==============================================================================

	## Finger control method
	# @param finger   MITTEN | FOREFINGER | THUMB
	# @param motorDir OPEN   | CLOSE		  		
	def fingerControl(self, finger, motorDir): 
		
		# TODO - TODO - While needs an output condition?
		logging.info("IOUTILS::fingerControl")
		
		""" With these three lines of code, the control of a single motor is achieved.
		First the feedback value of the controller is obtained from a specific channel
		of the ADC IC. Then, the control signal is computed with a PID. Finally, the
		control signal is applied to the motor as a PWM signal generated by the PWM IC.
		"""		
		# Initialize PID
		pid = PID(PID_KP, PID_KI, PID_KD)
		
		pid.setWindup = MOTOR_CTRL_MAX
		pid.setSampleTime = 0.2
		pid.SetPoint = 800;

		# Initialize buses
		# Re-init will be necessary?
		# self.adc = MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

		# Initialize PWM
		# Re-init will be necessary?
		#self.pwm = PCA9685.PCA9685(PCA_I2C_ADDR)
		#self.pwm.set_pwm_freq(PWM_FRQUENCY)

		logging.debug("IOUTILS::fingerControl - Reading from ADC Channel [%i]", FINGER_CHANNELS_MATRIX[ADC][finger])
					
		while True:
			feedback = getPotentiometerValyue()
			pid.update(feedback)
			duty_cycle = int(pid.output)
			self.motor_control(duty_cycle, finger, motorDir)			
    		
			
		
	## Include motorDir and test
	# To include motor direction management
	def motor_control(self, duty_cycle, finger, motorDir):
	
		logging.debug("IOUTILS::motorControl - Motor Control A [%i]", FINGER_MOTORS_MATRIX[finger][A])
		logging.debug("IOUTILS::motorControl - Motor Control B [%i]", FINGER_MOTORS_MATRIX[finger][B])
		logging.debug("IOUTILS::fingerControl - Reading from PWM Channel [%i]", FINGER_CHANNELS_MATRIX[PWM][finger])

		
		if(duty_cycle > MOTOR_CTRL_MAX):
			duty_cycle = MOTOR_CTRL_MAX
		elif(duty_cycle < -MOTOR_CTRL_MAX):
			duty_cycle = -MOTOR_CTRL_MAX
        
		if(duty_cycle >= 0):
			pwm.set_pwm(FINGER_CHANNELS_MATRIX[PWM][finger], 0, duty_cycle)
			GPIO.output(FINGER_MOTORS_MATRIX[finger][A], GPIO.LOW)  # set pin LOW
			GPIO.output(FINGER_MOTORS_MATRIX[finger][B], GPIO.HIGH)  # set pin HIGH
		else:
			pwm.set_pwm(FINGER_CHANNELS_MATRIX[PWM][finger], 0, abs(duty_cycle))  # set motor speed
			GPIO.output(FINGER_MOTORS_MATRIX[finger][A], GPIO.HIGH)  # set pin HIGH
			GPIO.output(FINGER_MOTORS_MATRIX[finger][B], GPIO.LOW)  # set pin LOW	
				
				
	## Read potentiometer position
	# @param finger MITTEN | FOREFINGER | THUMB
	def getPotentiometerValue(self, finger):
		
		logging.info("IOUTILS::getPotentiometerValue")	
		feedback = adc.read_adc(FINGER_CHANNELS_MATRIX[ADC][finger])
		return feedback

	## Retrieves a transition from MYO Sensor
	# @return transition TRANSITION_TO_INACTIVE | TRANSITION_TO_IDLE  | TRANSITION_TO_TONGS | TRANSITION_TO_FINGER   | TRANSITION_TO_CLOSE | TRANSITION_TO_FIST 
	def geTransitionFromMyo(self):		
		
		transition = self.myo.getMyoTransition()
		logging.info("IOUTILS::geTransitionFromMyo: %i", transition)
		return transition
	
