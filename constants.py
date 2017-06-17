import RPi.GPIO as GPIO


#==============================================================================
# GENERAL                                                                   
#==============================================================================

# Identifies open position
OPEN  = 0
# Identifies close position
CLOSE = 1

# Number of finger elements
FINGERS     = 3
# Identifies mitten fingers
MITTEN      = 0
# Identifies forefinger finger 
FOREFINGER  = 1
# Identifies thumb finger
THUMB       = 2

#==============================================================================
# STATES                                                                
#==============================================================================

# State Number
STATES_NUMBER   = 6
# Inactive state
STATE_INACTIVE  = 0
# Resting/Initial state. Open hand
STATE_IDLE      = 1
# Tongs state. Thumb + forefinger
STATE_TONGS     = 2
# Finger state. Forefinger
STATE_FINGER    = 3
# Close state. Mitten + forefinger
STATE_CLOSE     = 4
# Fist state. Mitten + forefinger + thumb
STATE_FIST      = 5


#==============================================================================
# TRANSITIONS                       
#==============================================================================

# Transition to inactive state
INVALID_TRANSITION     = -1
# Transition to inactive state
TRANSITION_TO_INACTIVE = 0
# Transition to resting/initial state
TRANSITION_TO_IDLE     = 1
# Transition to Tongs state
TRANSITION_TO_TONGS    = 2
# Transition to finger state
TRANSITION_TO_FINGER   = 3
# Transition to close state
TRANSITION_TO_CLOSE    = 4
# Transition to fist state
TRANSITION_TO_FIST     = 5

# Fingers position matrix from states definition
FINGER_POSITION_MATRIX = (
# MITTEN   FORE  THUMB
    ( OPEN,  OPEN,  OPEN  ), # STATE_INACTIVE
    ( OPEN,  OPEN,  OPEN  ), # STATE_IDLE
    ( OPEN,  CLOSE, CLOSE ), # STATE_TONGS
    ( CLOSE, OPEN,  CLOSE ), # STATE_FINGER
    ( CLOSE, CLOSE, OPEN  ), # STATE_CLOSE
    ( CLOSE, CLOSE, CLOSE )  # STATE_FIST
)


#==============================================================================
# MOTORS                                                                
#==============================================================================

# Min. Value for motors speed
MOTOR_SPEED_MIN = 0
# Max. Value for motors speed
MOTOR_SPEED_MAX = 255
# CONFIGURABLE VALUE: Motor Speed
MOTOR_SPEED     = 100

#==============================================================================
# PIN DESCRIPTION                                                           
#==============================================================================

#------------------------------------------------------------------------------
# OUTPUT
#------------------------------------------------------------------------------ 

# V_BAT_OK: LED Battery charge indicator for right levels
PIN_OUTPUT_LED_VBAT_OK   = 4

# V_BAT_LOW: LED Battery charge indicator for low level
PIN_OUTPUT_LED_VBAT_LOW = 17

# PW_Q: Pin for the power cut control
PIN_OUTPUT_POWER_CUT    = 27


#------------------------------------------------------------------------------
# INPUT
#------------------------------------------------------------------------------ 


# SW_TAC_0: Button for open hand
PIN_INPUT_BUTTON_0 = 19

# SW_TAC_1: Button for close hand
PIN_INPUT_BUTTON_1 = 26

# Switches to control states manually
# SW_DIP_0
PIN_INPUT_SWITCH_0 = 22
# SW_DIP_1
PIN_INPUT_SWITCH_1 =  5
# SW_DIP_2
PIN_INPUT_SWITCH_2 =  6
# SW_DIP_3
PIN_INPUT_SWITCH_3 = 13

#------------------------------------------------------------------------------
# BUSES
#------------------------------------------------------------------------------ 

# I2C PWM CIRCUITS (motors activation)
# SDA: I2C Data
PIN_BUS_SDA = 2
# SCL: I2C Clock
PIN_BUS_SCL = 3

# SPI: Serial Peripheral Interface Bus (Analog-Digital conversion)
# MOSI: Master Output Slave Input, or Master Out Slave In (data output from master)
PIN_BUS_MOSI   = 10
# MISO:  Master Input Slave Output, or Master In Slave Out (data output from slave)
PIN_BUS_MISO   =  9
# SCLK Serial Clock (output from master)
PIN_BUS_SCLK   = 11

# ADC_CS: Chip Select (reading from potentiometers)
PIN_BUS_ADC_CS = 7


#==============================================================================
# SWITCHES' RELATED STATES
#==============================================================================

STATE_BUTTON_0 = STATE_IDLE
STATE_BUTTON_1 = STATE_CLOSE

#==============================================================================
# FUNCTION MODES
#==============================================================================

# Keyboard control to initialize motors postion
INIT_MODE = 0
# Buttons control to test transitions
TEST_MODE = 1
# Myo operative control
OPERATION_MODE = 2

