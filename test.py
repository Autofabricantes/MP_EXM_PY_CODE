import logging
import time
import sys

from neopixel import *
import RPi.GPIO as GPIO

from constants import *

#******************************************************************************
# PUBLIC METHODS                                                             
#******************************************************************************

class Test:	
	
	def __init__(self):		
		
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(PIN_INPUT_SWITCH_0, GPIO.IN)
		GPIO.setup(PIN_INPUT_SWITCH_1, GPIO.IN)
		GPIO.setup(PIN_INPUT_SWITCH_2, GPIO.IN)
		GPIO.setup(PIN_INPUT_SWITCH_3, GPIO.IN)

		
		
	def testInputForTransitionKeyboard(self):
			
		logging.info("TEST::Transition to: ")
		logging.info(" (0) STATE_INACTIVE")
		logging.info(" (1) STATE_IDLE")
		logging.info(" (2) STATE_TONGS")
		logging.info(" (3) STATE_FINGER")
		logging.info(" (4) STATE_CLOSE")
		logging.info(" (5) STATE_FIST")
		logging.info(" (6) Exit")
		time.sleep(1)
		# read from keyboard

		transition = int(input("TEST::testInputForTransitionKeyboard - Introduce a value: "))
		
		if(transition == 6):
			sys.exit()
		
		return transition;
	
	
	def testInputForTransitionButtons(self):
			
		transition = INVALID_TRANSITION
				
		logging.info("\nTEST::testInputForTransitionButtons - Transition to... Press any button ")

		while (transition == INVALID_TRANSITION):
									 				
			if(GPIO.input(PIN_INPUT_BUTTON_0) == 0): 
				transition = STATE_BUTTON_0
			elif(GPIO.input(PIN_INPUT_BUTTON_1) == 0):
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
				
		
	