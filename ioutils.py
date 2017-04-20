import logging
import time
import constants

from test import Test
from state import State 

class InputOutputOutils:

#==============================================================================
# INITIALIZATION INPUT METHODS                                               
#==============================================================================

	def __init__(self):
		
		# TODELETE - Test Class
		self.test = Test();		
		# State to retrieve current finger's position
		self.currentState = State();
				

	# Initialization of INPUT sensors
	def initializeInputElements(self): 

		logging.debug("IOUTILS::initInput")


	# Reset of INPUT sensors
	def resetInputElements(self): 

		logging.debug("IOUTILS::resetInput")



#==============================================================================
# INITIALIZATION OUTPUT METHODS                                              
#==============================================================================

	# Initialization of OUTPUT elements
	def initializeOutputElements(self):

		logging.info("IOUTILS::initOutput")

		# TODO - RASPBERRY
		# Initialize motors pinout
		# pinMode(constants.MUX_A, constants.OUTPUT)
		# pinMode(constants.MUX_B, constants.OUTPUT)
		# pinMode(constants.MUX_C, constants.OUTPUT)

		# Initialize motors pinout
		# pinMode(constants.PIN_OUTPUT_MOTOR_MITTEN_PWM, constants.OUTPUT)
		# pinMode(constants.PIN_OUTPUT_MOTOR_MITTEN, constants.OUTPUT)
		# pinMode(constants.PIN_OUTPUT_MOTOR_FOREFINGER_PWM, constants.OUTPUT)
		# pinMode(constants.PIN_OUTPUT_MOTOR_FOREFINGER, constants.OUTPUT)
		# pinMode(constants.PIN_OUTPUT_MOTOR_THUMB_PWM, constants.OUTPUT)
		# pinMode(constants.PIN_OUTPUT_MOTOR_THUMB, constants.OUTPUT)
		
		logging.info("IOUTILS::initOutput - Initialize mitten")
		self.initialFingerControl(constants.MITTEN, constants.CONTROL_INPUT_POTENTIOMETER_MITTEN)
		time.sleep(1)

		logging.info("IOUTILS::initOutput - Initialize forefinger")
		self.initialFingerControl(constants.FOREFINGER, constants.CONTROL_INPUT_POTENTIOMETER_FOREFINGER)
		time.sleep(1)

		logging.info("IOUTILS::initOutput - Initialize thumb")
		self.initialFingerControl(constants.THUMB, constants.CONTROL_INPUT_POTENTIOMETER_THUMB)
		time.sleep(1)

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
		transitionTo = self.test.testInputForTransition()

		return transitionTo

	# Moves mitten to OPEN position if necessary
	def openMitten(self): 

		logging.debug("IOUTILS::openMitten")

		if(self.getMittenPosition() == constants.CLOSE):
			logging.info("IOUTILS::openMitten-OPEN")
			self.fingerControl(constants.MITTEN, constants.OPEN, constants.CONTROL_INPUT_POTENTIOMETER_MITTEN)
							
	# Moves mitten to CLOSE position if necessary
	def closeMitten(self):

		logging.debug("IOUTILS::closeMitten")

		if(self.getMittenPosition() == constants.OPEN):
			logging.info("IOUTILS::closeMitten - CLOSE");
			self.fingerControl(constants.MITTEN, constants.CLOSE, constants.CONTROL_INPUT_POTENTIOMETER_MITTEN)
	
	# Moves forefinger to OPEN position if necessary
	def openForefinger(self): 

		logging.debug("IOUTILS::openForefinger")

		if(self.getForefingerPosition() == constants.CLOSE):
			logging.debug("IOUTILS::openForefinger - OPEN")
			self.fingerControl(constants.FOREFINGER, constants.OPEN, constants.CONTROL_INPUT_POTENTIOMETER_FOREFINGER)
			
	# Moves forefinger to CLOSE position if necessary
	def closeForefinger(self):

		logging.debug("IOUTILS::closeForefinger")

		if(self.getForefingerPosition() == constants.OPEN):
			logging.debug("IOUTILS::closeForefinger - CLOSE")
			self.fingerControl(constants.FOREFINGER, constants.CLOSE, constants.CONTROL_INPUT_POTENTIOMETER_FOREFINGER)
			
	# Moves thumb to OPEN position if necessary
	def openThumb(self):

		logging.debug("IOUTILS::openThumb");

		if(self.getThumbPosition() == constants.CLOSE):
			logging.debug("IOUTILS::openThumb - OPEN")
			self.fingerControl(constants.THUMB, constants.OPEN, constants.CONTROL_INPUT_POTENTIOMETER_THUMB)
	
	# Moves mitten to CLOSE position if necessary
	def closeThumb(self):

		logging.debug("IOUTILS::closeThumb")

		if(self.getThumbPosition() == constants.CLOSE):
			logging.debug("IOUTILS::closeThumb - CLOSE")
			self.fingerControl(constants.THUMB, constants.CLOSE, constants.CONTROL_INPUT_POTENTIOMETER_THUMB)


#==============================================================================
# PCB CONTROLS                                                               
#==============================================================================

	# Initialize fingers position
	def initialFingerControl(self, motorId, controlId):

		logging.info("IOUTILS::initialFingerControl")

		initialPosition = self.multiplexorRead(controlId)
		finalPosition = initialPosition
		logging.info("IOUTILS::initialFingerControl - Initial position: %i", initialPosition)

		if(finalPosition < 200):
			while(finalPosition < 200):
				self.motorControl(motorId, constants.OPEN, 100);
				time.sleep(0.1);
				finalPosition = self.multiplexorRead(controlId)
				self.motorControl(motorId, constants.OPEN, constants.MOTOR_SPEED_MIN)
				
		elif(finalPosition > 500):
			while(finalPosition > 500):
				self.motorControl(motorId, constants.CLOSE, 100)
				time.sleep(0.1)
				finalPosition = self.multiplexorRead(controlId)
				self.motorControl(motorId, constants.CLOSE, constants.MOTOR_SPEED_MIN);
	

		logging.info("IOUTILS::initialFingerControl - Final position: %i", finalPosition)


	# Finger control method
	def fingerControl(self, motorId, motorDir, controlId):

		initialPosition = self.multiplexorRead(controlId)
		finalPosition = initialPosition
		logging.info("IOUTILS::fingerControl - Initial position: %i", initialPosition)

		
		if((finalPosition > 200) and (motorDir == constants.OPEN)):

			self.motorControl(motorId, constants.OPEN , constants.MOTOR_SPEED)
			time.sleep(1.5)
			self.motorControl(motorId, constants.OPEN, constants.MOTOR_SPEED_MIN)
			finalPosition = self.multiplexorRead(controlId)

		elif ((finalPosition < 800) and (motorDir == constants.CLOSE)):

			self.motorControl(motorId, constants.CLOSE , constants.MOTOR_SPEED)
			time.sleep(1.5)
			self.motorControl(motorId, constants.CLOSE, constants.MOTOR_SPEED_MIN)
			finalPosition = self.multiplexorRead(controlId)

		else:
			self.initialFingerControl(motorId, controlId)
			self.fingerControl(motorId, motorDir, controlId)
	

		logging.info("IOUTILS::fingerControl - Final position: %i", finalPosition)
		

	# Motor Control method
	def motorControl(self, motorID, motorDir, motorSpeed): 

		logging.info("IOUTILS::motorControl")

		# Forward Direction --> CLOSE --> 1
		# 1024 --> 0 (decrements)
		if(motorDir): 
			logging.info("IOUTILS::motorControl - Forward direction - CLOSE")
			# TODO - RASPBERRY
			# digitalWrite(constants.MOTOR_CONTROL_MATRIX[motorID][1], LOW)
			# analogWrite(constants.MOTOR_CONTROL_MATRIX[motorID][0], motorSpeed)
			# Backward Direction --> OPEN --> 0
			# 0 --> 1024 (increments)
		else:
			logging.info("IOUTILS::motorControl - Backward direction - OPEN")
			# TODO - RASPBERRY
			# digitalWrite(constants.MOTOR_CONTROL_MATRIX[motorID][1], constants.HIGH)
			# analogWrite(constants.MOTOR_CONTROL_MATRIX[motorID][0], (constants.MOTOR_SPEED_MAX - motorSpeed))
	
	

	#  Multiplexor read method
	def multiplexorRead(self, controlId):

		# Main Multiplexer (vs Acc Multiplexer)
		
		# Lecture Sensors through 74HC4051 Multiplexer
		# Entry channel selection for 74HC4051
	
		logging.info("IOUTILS::multiplexorRead - Input: %i", controlId)

		#cA = controlId & 0x01;   
		#cB = (controlId>>1) & 0x01;     
		#cC = (controlId>>2) & 0x01;   
	
		# TODO - RASPBERRY
		# digitalWrite(MUX_A, cA);
		# digitalWrite(MUX_B, cB);
		# digitalWrite(MUX_C, cC);
		
		# readedValue = analogRead(MUX_MAIN)

		# logging.info("IOUTILS::multiplexorRead - Output: %i", readedValue)
	
		# TODO - RASPBERRY
		# TODELETE
		return 400
		#return readedValue
