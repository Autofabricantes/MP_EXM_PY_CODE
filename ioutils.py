import logging
import time
import constants

from numpy import interp

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
	
		logging.info("IOUTILS::initialFingerControlPID")
		
		input = interp(self.multiplexorRead(controlId), [0, 1024], [constants.MOTOR_SPEED_MIN, constants.MOTOR_SPEED])
		logging.info("IOUTILS::initialFingerControlPID - input: %f", input)

		setpoint = 0
		logger.info("IOUTILS::initialFingerControlPID - initialization setpoint: %f", setpoint)

		if(input > 0):
			#pid = PID(input, output, setpoint, PID_KP, PID_KI, PID_KD, REVERSE)
			motorDir = constants.OPEN
	

		#Turn on the PID loop
		#pid.SetMode(AUTOMATIC)
		#pid.SetOutputLimits(0,MOTOR_SPEED)

		while(abs(input - setpoint) >  PID_LIMITS):

			input = interp(self.multiplexorRead(controlId), [0, 1024], [constants.MOTOR_SPEED_MIN, constants.MOTOR_SPEED])
			#input = multiplexorRead(controlId);

			#pid.Compute()

			motorControl(motorId, motorDir, round(output))

			input = interp(self.multiplexorRead(controlId), [0, 1024], [constants.MOTOR_SPEED_MIN, constants.MOTOR_SPEED])
			#input = multiplexorRead(controlId);
			logger.info("IOUTILS::initialFingerControlPID - loop input: %f", input);
			logger.info("IOUTILS::initialFingerControlPID - loop output: %f", output)

		logging.info("IOUTILS::initialFingerControlPID - Stop motor")
		self.motorControl(motorId, motorDir, constants.MOTOR_SPEED_MIN)



	# Finger control method
	def fingerControl(self, motorId, motorDir, controlId):
		
		# logging.info("IOUTILS::fingerControlPID")		
		
		#input = interp(multiplexorRead(controlId), [0, 1024], [constants.MOTOR_SPEED_MIN, constants.MOTOR_SPEED])		
	    #input = multiplexorRead.multiplexorRead(controlId)
	    
   	    #logging.info("IOUTILS::fingerControlPID - input: %f", input)
   	    
   	    if (motorDir == constants.OPEN):	    	   	    	    		
   	    	setpoint = constants.MOTOR_SPEED_MIN
   	    	logging.info("IOUTILS::fingerControlPID - OPEN - final setpoint: %f", setpoint)
   	    	   	    	
   	    else:
    	 	setpoint = constants.MOTOR_SPEED
    	 	logging.info("IOUTILS::fingerControlPID - CLOSE - final setpoint: %f", setpoint)  
    		# Initialize PID
    	 	# pid = PID(&input, &output, &setpoint, PID_KP, PID_KI, PID_KD, DIRECT)
    	 	    	 			
    	# Turn on the PID loop
     	# pid.SetMode(AUTOMATIC)
      	# pid.SetOutputLimits(0, MOTOR_SPEED)
      	
		while(abs(input - setpoint) >  constants.PID_LIMITS):

		  	input = interp(self.multiplexorRead(controlId),[0,1023],[constants.MOTOR_SPEED_MIN, constants.MOTOR_SPEED])
    	  	#input = multiplexorRead(controlId);

    	 	logger.info("IOUTILS::fingerControlPID - input: %f", input)

    	 	#pid.Compute();
      
    	 	self.motorControl(motorId, motorDir, round(output))

    	 	logging.info("IOUTILS::fingerControlPID - output: %f", output)
    	 	
    	logging.info("IOUTILS::fingerControlPID - Stopping motor")
    	self.motorControl(motorId, motorDir, constants.MOTOR_SPEED_MIN)



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
