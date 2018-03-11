import logging
import time
import sys
import threading

from neopixel import *
import RPi.GPIO as GPIO

#from Adafruit_MCP3008 import MCP3008
#from Adafruit_PCA9685 import PCA9685

from constants import *
from myoutils import Myoutils

#******************************************************************************
# PUBLIC METHODS															 
#******************************************************************************

## Test class
class Test:	
	
	## Initialization
	def __init__(self, myo=0):	
		logging.info("TEST::init")	
		#adc = MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
		
		self.myo = myo
		
	## Testing from keyboard
	def testInputForTransitionKeyboard(self):
			
		logging.info("\n\nTEST::Transition to: ")
		
		logging.info(" (0) STATE_INACTIVE")
		logging.info(" (1) STATE_IDLE")
		logging.info(" (2) STATE_TONGS")
		logging.info(" (3) STATE_FINGER")
		logging.info(" (4) STATE_CLOSE")
		logging.info(" (5) STATE_FIST")		
		
		logging.info(" (6) INITIALIZE SENSORS ")

		logging.info(" (7) TEST FOR POTENTIOMETER")
		logging.info(" (8) TEST FOR MOTOR")
		logging.info(" (9) TEST MYO")
		
		logging.info("(10) EXIT")

		
		time.sleep(1)		

		transition = int(input("TEST::testInputForTransitionKeyboard - Introduce a value: "))
		
		if(transition == 6):
			self.testPotentiometer()
			self.testInputForTransitionKeyboard()
						
		elif(transition == 7):
			self.testMotor()
			self.testInputForTransitionKeyboard()

		elif(transition == 8):
			self.testInputForTransitionKeyboard()
			
		elif(transition == 9):
			self.testMyo()
			self.testInputForTransitionKeyboard()
		
		elif(transition == 10):
			sys.exit()
		
		return transition
	
	## Testing from transition buttons
	"""
	def testInputForTransitionButtons(self):
 			
 		transition = INVALID_TRANSITION
 				
 		logging.info("\nTEST::testInputForTransitionButtons - Transition to... Press any button ")
 
 		while (transition == INVALID_TRANSITION):
 									 				
 			if(GPIO.input(GPIO_INPUT_BUTTON_0) == 0): 
 				transition = STATE_BUTTON_0
 			elif(GPIO.input(GPIO_INPUT_BUTTON_1) == 0):
 				transition = STATE_BUTTON_1										
 						   
 		time.sleep(1)
 		
 		return transition
	"""
	
	## Testing potentiometer		
	def testPotentiometer(self):

		#adc = MCP3008(clk=PIN_CLK, cs=PIN_CS, miso=PIN_MISO, mosi=PIN_MOSI)

		while(True):
			
			try:
			
				#feedback = adc.read_adc(THUMB_MPOT_0)
				#print(feedback)
				time.sleep(0.5)
			
			except Exception as err:
				print(err)
				break

	## Testing motor
	def testMotor(self):
		
		#pwm = PCA9685()
		#pwm.set_pwm_freq(60) 
		
		while(True):
			try:
				#duty_cycle = int(input("Enter PWM duty cycle (min: -4096, max: 4096): "))
				duty_cycle = 0
				motor_control(duty_cycle)
			except Exception as err:
				print(err)
				break
		   			
	## Testing motor control   
	def motor_control(self, duty_cycle):
		
		if(duty_cycle >= 0):
			return
			#pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][A], 0, duty_cycle)
			#pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][B], 0, MOTOR_CTRL_MIN)  # set pin LOW
			
		else:
			return
			#pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][A], 0, abs(duty_cycle))
			#pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][B], 0, MOTOR_CTRL_MAX)  # set pin HIGH
			
	## Testing Mio
	def testMyo(self):		
		logging.info("TEST::Testing Myo")
		self.myo.startThreadMyo()
		self.myo.joinThreadMyo(10000)
		
		


		
