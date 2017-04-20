import logging
import time
#from neopixel import *

#******************************************************************************
# PUBLIC METHODS                                                             
#******************************************************************************

class Test:	
		
	def testInputForTransition(self):
			
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
		
		return transition;
	

	def testInitializeLedStripe(self):
		
		logging.info("TEST::testInitializeLedStripe")
		
		#TODO - RASPBERRY
		#ledStripe = Adafruit_NeoPixel(10, PIN_OUTPUT_LEDSTRIPE_RGB, NEO_GRB + NEO_KHZ800)
		#ledStripe.begin()

		#ledStripe.setBrightness(50)
		#ledStripe.setPixelColor(0, ledStripe.Color(0, 0, 0))
		#ledStripe.show()

	
	def testOutputWithLedStripe(self, pos, r, g, b):
		
		logging.info("TEST::testOutputWithLedStripe")
		
		#TODO - RASPBERRY
		#ledStripe.setPixelColor(0, ledStripe.Color(r, g, b))
		#ledStripe.show()
	


