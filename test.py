import logging
import time
import sys

from neopixel import *
import RPi.GPIO as GPIO

from Adafruit_MCP3008 import MCP3008
from Adafruit_PCA9685 import PCA9685

from constants import *

#******************************************************************************
# PUBLIC METHODS                                                             
#******************************************************************************

class Test:	
	
	def __init__(self):	
		logging.info("TEST::init: ")					
		#adc = MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
		
	def testInputForTransitionKeyboard(self):
			
		logging.info("TEST::Transition to: ")
		logging.info(" (0) STATE_INACTIVE")
		logging.info(" (1) STATE_IDLE")
		logging.info(" (2) STATE_TONGS")
		logging.info(" (3) STATE_FINGER")
		logging.info(" (4) STATE_CLOSE")
		logging.info(" (5) STATE_FIST")		
		
		logging.info(" (6) TEST FOR POTENTIOMETER")
		logging.info(" (7) TEST FOR MOTOR")
				
		logging.info(" (8) Exit")
		time.sleep(1)		

		transition = int(input("TEST::testInputForTransitionKeyboard - Introduce a value: "))
		
		if(transition == 6):
			self.testPotentiometer()
			self.testInputForTransitionKeyboard()
						
		elif(transition == 7):
			self.testMotor()
			self.testInputForTransitionKeyboard()
						
		if(transition == 8):
			sys.exit()
		
		return transition;
	
	
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
	
	

	def testInitializeLedStripe(self):
		
		logging.info("TEST::testInitializeLedStripe")
		
		"""
		LED_COUNT   = 1       # Number of LED pixels.
		LED_PIN     = 3       # GPIO pin connected to the pixels (must support PWM!).
		LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
		LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
		LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)
		
		ledStripe = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
		ledStripe.begin()

		ledStripe.setBrightness(50)
		ledStripe.setPixelColor(0, ledStripe.Color(0, 0, 0))
		ledStripe.show()
		"""

	
	def testOutputWithLedStripe(self, pos, r, g, b):
		
		logging.info("TEST::testOutputWithLedStripe")
		
		"""
		ledStripe.setPixelColor(0, ledStripe.Color(r, g, b))
		ledStripe.show()
		"""
				
	def testPotentiometer(self):

		adc = MCP3008(clk=PIN_CLK, cs=PIN_CS, miso=PIN_MISO, mosi=PIN_MOSI)

		while(True):
			
			try:
			
				feedback = adc.read_adc(THUMB_MPOT_0)
				print(feedback)
				time.sleep(0.5)
			
			except Exception as err:
				print(err)
				break


	def testMotor(self):
		
		pwm = PCA9685()
		pwm.set_pwm_freq(60) 
		
		while(True):
			try:
				duty_cycle = int(input("Enter PWM duty cycle (min: -4096, max: 4096): "))
				motor_control(duty_cycle)
			except Exception as err:
				print(err)
				break
		   			   
	def motor_control(duty_cycle):
		
		if(duty_cycle >= 0):
			pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][A], 0, duty_cycle)
			pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][B], 0, MOTOR_CTRL_MIN)  # set pin LOW
			
		else:
			pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][A], 0, abs(duty_cycle))
			pwm.set_pwm(FINGER_MOTORS_MATRIX[THUMB][B], 0, MOTOR_CTRL_MAX)  # set pin HIGH


