import logging

from constants import *

class State:
		
#==============================================================================
# PUBLIC METHODS                                                             
#==============================================================================

	def __init__(self):

		logging.debug("STATE::State");
		# Current state
		self.currentState = STATE_INACTIVE;

	# Resets current state
	def reset(self):
		logging.debug("STATE::reset")
		self.currentState = STATE_INACTIVE
		
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
		
		fingerPosition = FINGER_POSITION_MATRIX[self.currentState][MITTEN]
		logging.info("STATE::getMittenPos - State[%i] - Position[%i]", self.currentState,fingerPosition)

		return fingerPosition;


	# Detects forefinger position depending on
	# current state
	def getForefingerPosition(self):
		
		fingerPosition   = FINGER_POSITION_MATRIX[self.currentState][FOREFINGER]
		logging.debug("STATE::getForefingerPos - State[%i] - Position[%i]", self.currentState,fingerPosition)
		
		return fingerPosition


	# Detects thumb position from
	# current state
	def getThumbPosition(self):
		
		fingerPosition   = FINGER_POSITION_MATRIX[self.currentState][THUMB]
		logging.debug("STATE::getThumbPos - State[%i] - Position[%i]", self.currentState,fingerPosition)

		return fingerPosition

