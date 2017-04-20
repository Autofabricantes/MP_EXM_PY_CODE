import constants
import logging

class State:
		
#==============================================================================
# PUBLIC METHODS                                                             
#==============================================================================

	def __init__(self):

		logging.debug("STATE::State");
		# Current state
		self.currentState = constants.STATE_INACTIVE;

	# Resets current state
	def reset(self):
		logging.debug("STATE::reset")
		self.currentState = constants.STATE_INACTIVE
		
	# Getter
	def getCurrentState(self):

		logging.debug("STATE::getCurrentState: %i", self.currentState)
		return self.currentState

	# Setter
	def setCurrentState(self, state):

		logging.info("STATE::setCurrentState: %i", state)
		self.currentState = state


	# Detects mitten position depending on
	# current state
	def getMittenPosition(self):
		
		fingerPosition = constants.FINGER_POSITION_MATRIX[self.currentState][constants.MITTEN]
		logging.info("STATE::getMittenPos - State[%i] - Position[%i]", self.currentState,fingerPosition)

		return fingerPosition;


	# Detects forefinger position depending on
	# current state
	def getForefingerPosition(self):
		
		fingerPosition   = constants.FINGER_POSITION_MATRIX[self.currentState][constants.FOREFINGER]
		logging.debug("STATE::getForefingerPos - State[%i] - Position[%i]", self.currentState,fingerPosition)
		
		return fingerPosition


	# Detects thumb position from
	# current state
	def getThumbPosition(self):
		
		fingerPosition   = constants.FINGER_POSITION_MATRIX[self.currentState][constants.THUMB]
		logging.debug("STATE::getThumbPos - State[%i] - Position[%i]", self.currentState,fingerPosition)

		return fingerPosition

