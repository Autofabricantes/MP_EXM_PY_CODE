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
STATES_NUMBER  = 6
# Inactive state
STATE_INACTIVE = 0
# Resting/Initial state. Open hand
STATE_IDLE      = 1
# Tongs state. Thumb + forefinger
STATE_TONGS   = 2
# Finger state. Forefinger
STATE_FINGER  = 3
# Close state. Mitten + forefinger
STATE_CLOSE   = 4
# Fist state. Mitten + forefinger + thumb
STATE_FIST    = 5


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
MOTOR_SPEED = 100


#==============================================================================
# PIN DESCRIPTION                                                           
#==============================================================================

# OUTPUT pin for LED RGB
PIN_OUTPUT_LED_RGB = 13
PIN_OUTPUT_LEDSTRIPE_RGB = 10                        

# Accesory Board Detection
# int ACC_BRD
# Multiplexer Control Crazy Pionut Assignement A
MUX_A = 16 
# Multiplexer Control Crazy Pionut Assignement B
MUX_B = 14 
# Multiplexer Control Crazy Pionut Assignement C
MUX_C = 15 
# Main Board Multiplexer Output
MUX_MAIN = 0
# Acc Board Multiplexer Output 
MUX_ACC = 1 

# INPUT pin for mitten related potentiometer
PIN_OUTPUT_POTENTIOMETER_MITTEN = 2
# INPUT pin for forefinger related potentiometer
PIN_OUTPUT_POTENTIOMETER_FOREFINGER = 4
# INPUT pin for thumb related potentiometer
PIN_OUTPUT_POTENTIOMETER_THUMB = 6

# INPUT pin for mitten related amperimeter
PIN_OUTPUT_CURRENT_SENSOR_MITTEN = 3
# INPUT pin for forefinger related amperimeter
PIN_OUTPUT_CURRENT_SENSOR_FOREFINGER = 5
# INPUT pin for thumb related amperimeter
PIN_OUTPUT_CURRENT_SENSOR_THUMB = 7

# OUTPUT pin for mitten related motor
PIN_OUTPUT_MOTOR_MITTEN_PWM = 9
PIN_OUTPUT_MOTOR_MITTEN = 8
# OUTPUT pin for forefinger related motor
PIN_OUTPUT_MOTOR_FOREFINGER_PWM = 5
PIN_OUTPUT_MOTOR_FOREFINGER = 7
# OUTPUT pin for thumb related motor
PIN_OUTPUT_MOTOR_THUMB_PWM = 3
PIN_OUTPUT_MOTOR_THUMB = 4

#==============================================================================
# Multiplexor Control Matrix
#==============================================================================

MOTOR_CONTROL_MATRIX = (
    (PIN_OUTPUT_MOTOR_MITTEN_PWM, PIN_OUTPUT_MOTOR_MITTEN),
    (PIN_OUTPUT_MOTOR_FOREFINGER_PWM, PIN_OUTPUT_MOTOR_FOREFINGER),
    (PIN_OUTPUT_MOTOR_THUMB_PWM, PIN_OUTPUT_MOTOR_THUMB)
)

# MPOT_0
CONTROL_INPUT_POTENTIOMETER_MITTEN = 2
# CS_0
CONTROL_INPUT_CURRENT_SENSOR_MITTEN = 3
# MPOT_1
CONTROL_INPUT_POTENTIOMETER_FOREFINGER = 4
# CS_1
CONTROL_INPUT_CURRENT_SENSOR_FOREFINGER = 5
# MPOT_2
CONTROL_INPUT_POTENTIOMETER_THUMB = 6
# CS_2
CONTROL_INPUT_CURRENT_SENSOR_THUMB = 7
