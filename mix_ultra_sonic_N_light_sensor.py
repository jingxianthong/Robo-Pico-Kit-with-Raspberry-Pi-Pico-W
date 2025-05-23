'''
Obstacle Avoidance Robot using 3V-5.5V SR04P Ultrasonic Ranging Module.
Additional Library:
    - adafruit_hcsr04.mpy
    - adafruit_motor
'''

import time
import board
import digitalio
import pwmio
from adafruit_motor import motor
import adafruit_hcsr04
import analogio

# Ultrasonic Sensor Setup
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)

# Left Motor
PWM_M1A = board.GP8
PWM_M1B = board.GP9
# Right Motor
PWM_M2A = board.GP10
PWM_M2B = board.GP11

# DC motor setup
pwm_1a = pwmio.PWMOut(PWM_M1A, frequency=10000)
pwm_1b = pwmio.PWMOut(PWM_M1B, frequency=10000)
motorL = motor.DCMotor(pwm_1a, pwm_1b)
pwm_2a = pwmio.PWMOut(PWM_M2A, frequency=10000)
pwm_2b = pwmio.PWMOut(PWM_M2B, frequency=10000)
motorR = motor.DCMotor(pwm_2a, pwm_2b)

# light sensor port
ldr = analogio.AnalogIn(board.GP27)
######################################################################################

def Robot_Movement(sL, sR):
    motorL.throttle = sL
    motorR.throttle = sR
    
def Read_Ultrasonic():
    time.sleep(0.1)
    return sonar.distance

def backward():
    Robot_Movement(-0.5,-0.5)
    time.sleep(1)
    
def backward_left():    
    Robot_Movement(-0.3,-0.7)
    time.sleep(1)       

def  TurnLeft():
  Robot_Movement(0.1, 0.5)


def forward():
    Robot_Movement(0.5, 0.54)

def stop():
  Robot_Movement(0, 0)

######################################################################################

while True:
    raw = ldr.value
    print("raw = {:5d}".format(raw))
    time.sleep(0.1)
    try:
        if (raw > 35000):
            backward()   # Backward
            backward_left() # Backward left
            
        Distance = Read_Ultrasonic()
        print(f"Distance: {Distance} cm")
        
        if Distance < 20:  # Obstacle detected
            TurnLeft()  # Turn Left
            time.sleep(1)
        else:  # No obstacle
            forward()  # Move Forward
        
    except RuntimeError:
        print("Ultrasonic sensor error. Retrying...")
        stop()  # Stop in case of sensor error
        time.sleep(0.1)
