import logging
import time
from neopixel import *
import RPi.GPIO as GPIO

import constants


#******************************************************************************
# PUBLIC METHODS                                                             
#******************************************************************************

class Test:	
	
	def __init__(self):		
		
		#GPIO.setmode(GPIO.BOARD)	
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(constants.PIN_INPUT_SWITCH_0, GPIO.IN)
		GPIO.setup(constants.PIN_INPUT_SWITCH_1, GPIO.IN)
		GPIO.setup(constants.PIN_INPUT_SWITCH_2, GPIO.IN)
		GPIO.setup(constants.PIN_INPUT_SWITCH_3, GPIO.IN)

		
		
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

		transition = int(input("Introduce a value: "))
		
		if(transition == 6):
			exit
		
		return transition;
	
	
	def testInputForTransitionButtons(self):
			
		transition = constants.INVALID_TRANSITION
		
		
		while (transition == constants.INVALID_TRANSITION):
			
			time.sleep(1)
			
			logging.info("TEST::Transition to... Press any button ")

			# Podría incluir el boton de reset como INNACTIVE
					
			if(GPIO.input(constants.PIN_INPUT_SWITCH_0) == 1): 
				transition = constants.STATE_SWITCH_0
			elif(GPIO.input(constants.PIN_INPUT_SWITCH_1) == 1):
				transition = constants.STATE_SWITCH_1
			elif(GPIO.input(constants.PIN_INPUT_SWITCH_2) == 1):
				transition = constants.STATE_SWITCH_2
			elif(GPIO.input(constants.PIN_INPUT_SWITCH_3) == 1):
				transition = constants.STATE_SWITCH_3
			else:
				logging.info("TEST::Any value red, begin again ")					
						   
		return transition;
	
	

	def testInitializeLedStripe(self):
		
		logging.info("TEST::testInitializeLedStripe")
		
		#ledStripe = Adafruit_NeoPixel(10, PIN_OUTPUT_LEDSTRIPE_RGB, NEO_GRB + NEO_KHZ800)
		#ledStripe.begin()

		#ledStripe.setBrightness(50)
		#ledStripe.setPixelColor(0, ledStripe.Color(0, 0, 0))
		#ledStripe.show()

	
	def testOutputWithLedStripe(self, pos, r, g, b):
		
		logging.info("TEST::testOutputWithLedStripe")
		
		#ledStripe.setPixelColor(0, ledStripe.Color(r, g, b))
		#ledStripe.show()
	