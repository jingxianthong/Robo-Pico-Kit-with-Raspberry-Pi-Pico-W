'''
Basic Robot Movement using Maker Drive and CircuitPython on Pi Pico W.

Libraries required from bundle (https://circuitpython.org/libraries):
  - adafruit_motor
  
References:
  - https://learn.adafruit.com/circuitpython-essentials/circuitpython-pwm
  - https://my.cytron.io/tutorial/control-dc-motor-using-maker-drive-and-circuitpython-on-rp2040
  
'''

import time
import board
import analogio
import digitalio
import pwmio
from adafruit_motor import motor


# Left Motor
PWM_M1A = board.GP8
PWM_M1B = board.GP9
# Right Motor
PWM_M2A = board.GP10
PWM_M2B = board.GP11



# DC motor setup
# DC Motors generate electrical noise when running that can reset the microcontroller in extreme
# cases. A capacitor can be used to help prevent this.
pwm_1a = pwmio.PWMOut(PWM_M1A, frequency=10000)
pwm_1b = pwmio.PWMOut(PWM_M1B, frequency=10000)
motorL = motor.DCMotor(pwm_1a, pwm_1b)
pwm_2a = pwmio.PWMOut(PWM_M2A, frequency=10000)
pwm_2b = pwmio.PWMOut(PWM_M2B, frequency=10000)
motorR = motor.DCMotor(pwm_2a, pwm_2b)

ldr = analogio.AnalogIn(board.GP27)

SA = analogio.AnalogIn(board.GP26)


def Robot_Movement(sL, sR):
    motorL.throttle = sL
    motorR.throttle = sR

def forward():
    Robot_Movement(0.5, 0.54)
    time.sleep(3)

def Backward():
  Robot_Movement(-0.5, -0.52)
  time.sleep(3)

def  TurnLeft():
  Robot_Movement(0.1, 0.5)
  time.sleep(3)

def TurnRight():
  Robot_Movement(0.5, 0.1)
  time.sleep(3)

def stop():
  Robot_Movement(0, 0)
  time.sleep(3)
print("Press GP20 button to start...")


while True:  # Button pressed (logic is active low)
   forward()
   Backward()
   TurnLeft()
   TurnRight()
   stop()


