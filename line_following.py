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
    Robot_Movement(1.0, 1.0)

def Backward():
  Robot_Movement(-0.5, -0.52)
  time.sleep(3)


#####################################################
# Turn left
def TurnLeft():
  Robot_Movement(0.6, 0.2)


def hardleft():
  Robot_Movement(0.2, 0.63)\

def superhardleft():
  Robot_Movement(0, 0.64)
#######################################################
#### Turn Right
def TurnRight():
  Robot_Movement(0.5, 0.3)


def HardRight():
  Robot_Movement(0.6, 0)

############
def stop():
  Robot_Movement(0, 0)
  time.sleep(3)


############################################################################################################################################################################
while True:
    an = (SA.value * 3.3) / 65536
    print(an)
    if 1.4 < an < 1.5:  # 1.4 - 1.7v
        forward()
    elif 1.8 < an < 2.2:  # 1.7 - 2.2v
        TurnRight()
    elif 0.8 < an < 1.4:  # 0.8 - 1.4v
        forward()
    elif 2.2 < an < 2.85:  # 2.2 - 2.85v
        HardRight()
    elif 0.4 < an < 0.8:  # 0.6 - 0.8v
        hardleft()
    elif 2.85 < an < 3.0:  # 2.85 - 3.0v
        HardRight()
    elif 0.3 < an < 0.4:  # 0.3 - 0.4v
        superhardleft()
    # Continue without movement
    elif an < 0.3 or an > 3:  # <0.3v or >3V
      continue
  
