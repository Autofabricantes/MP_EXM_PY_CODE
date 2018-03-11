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
# Identifies thumb finger
THUMB       = 0
# Identifies forefinger finger 
FOREFINGER  = 1
# Identifies mitten fingers
MITTEN      = 2



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
TRANSITION_TO_INACTIVE =  0
# Transition to resting/initial state
TRANSITION_TO_IDLE     =  1
# Transition to Tongs state
TRANSITION_TO_TONGS    =  2
# Transition to finger state
TRANSITION_TO_FINGER   =  3
# Transition to close state
TRANSITION_TO_CLOSE    =  4
# Transition to fist state
TRANSITION_TO_FIST     =  5
# No identified movement intention
TRANSITION_TO_NOTHING  = 6

# Fingers position matrix from states definition
FINGER_POSITION_MATRIX = (
    # THUMB  FORE   MITTEN
    ( OPEN,  OPEN,  OPEN  ), # STATE_INACTIVE
    ( OPEN,  OPEN,  OPEN  ), # STATE_IDLE
    ( CLOSE, CLOSE, OPEN  ), # STATE_TONGS
    ( CLOSE, OPEN,  CLOSE ), # STATE_FINGER
    ( OPEN, CLOSE,  CLOSE ), # STATE_CLOSE
    ( CLOSE, CLOSE, CLOSE )  # STATE_FIST
)

#==============================================================================
# PIN DESCRIPTION                                                           
#==============================================================================

#------------------------------------------------------------------------------
# OUTPUT
#------------------------------------------------------------------------------ 

# V_BAT_OK: LED Battery charge indicator for right levels
GPIO_OUTPUT_LED_VBAT_OK   = 4

# V_BAT_LOW: LED Battery charge indicator for low level
GPIO_OUTPUT_LED_VBAT_LOW = 17

# PW_Q: Pin for the power cut control
GPIO_OUTPUT_POWER_CUT    = 27


#------------------------------------------------------------------------------
# INPUT
#------------------------------------------------------------------------------ 


# SW_TAC_0: Button for open hand
GPIO_INPUT_BUTTON_0 = 19

# SW_TAC_1: Button for close hand
GPIO_INPUT_BUTTON_1 = 26

# Switches to control states manually
# SW_DIP_0
GPIO_INPUT_SWITCH_0 = 22
# SW_DIP_1
GPIO_INPUT_SWITCH_1 =  5
# SW_DIP_2
GPIO_INPUT_SWITCH_2 =  6
# SW_DIP_3
GPIO_INPUT_SWITCH_3 = 13

#------------------------------------------------------------------------------
# BUSES
#------------------------------------------------------------------------------ 

# I2C PWM CIRCUITS (motors activation)
# SDA: I2C Data
GPIO_BUS_SDA = 2
# SCL: I2C Clock
GPIO_BUS_SCL = 3

# SPI: Serial Peripheral Interface Bus (Analog-Digital conversion)
# MOSI: Master Output Slave Input, or Master Out Slave In (data output from master)
GPIO_BUS_MOSI   = 10
# MISO:  Master Input Slave Output, or Master In Slave Out (data output from slave)
GPIO_BUS_MISO   =  9
# SCLK Serial Clock (output from master)
GPIO_BUS_SCLK   = 11

# ADC_CS: Chip Select (reading from potentiometers)
GPIO_BUS_ADC_CS = 7

# Software SPI configuration for the MCP3008 - Physical pins
PIN_CLK  = 18
PIN_MISO = 23
PIN_MOSI = 24
PIN_CS   = 25


#------------------------------------------------------------------------------
# POTENTIOMETERS (ADC CIRCUIT PIONOUT)
#------------------------------------------------------------------------------ 

THUMB_MPOT_0 = 2
FOREFINGER_MPOT_1 = 3 
MITTEN_MPOT_2 = 4

#------------------------------------------------------------------------------
# MOTORS (PWM CIRCUIT PINOUT)
#------------------------------------------------------------------------------ 

MOTOR_CTRL_MIN = 0  
MOTOR_CTRL_MAX = 4096 


# THUMB_MOT_X_A_CTRL and THUMB_MOT_X_B_CTRL
A = 0
B = 1 

# TODO - Verify values
FINGER_MOTORS_MATRIX = (
    #     A      B
    (     6,     7), # THUMB    
    (     8,     9), # FORE
    (    10,    11)  # MITTEN
)


#------------------------------------------------------------------------------
# FINGER'S CHANNELS
#------------------------------------------------------------------------------ 

ADC = 0
PWM = 1

# TODO - Verify values
FINGER_CHANNELS_MATRIX = (
    #  THUMB  FORE  MITTEN  
    (     0,     1,     2), # ADC
    (     3,     4,     5)  # PWM
)


#==============================================================================
# SWITCHES' RELATED STATES
#==============================================================================

STATE_BUTTON_0 = STATE_IDLE
STATE_BUTTON_1 = STATE_CLOSE

#==============================================================================
# FUNCTION MODES
#==============================================================================

# Buttons control to test and initialize
TEST_MODE = 0
# Myo operative control
OPERATION_MODE = 1


#==============================================================================
# PID
#==============================================================================

PID_KP = 10
PID_KI = 0
PID_KD = 0


