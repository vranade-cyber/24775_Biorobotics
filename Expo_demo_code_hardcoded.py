from __future__ import division
from adafruit_servokit import ServoKit

import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)
kit = ServoKit(channels=16)

def move_patch(pin,step,size):  # PWM values between 307 and 409 for disengaging gecko
    pwm.set_pwm(pin, 0, step)   # PWM values between 205 and 307 to engage this patch
    time.sleep(size)           # Just add pin and value to use this part
    pwm.set_pwm(pin,0,307)       # This is necessary!!! If not code will go into a for Loop
    time.sleep(1)              # Same condition 
    return 1

def move_leg(pin,degree):      # Set Pin and degree of rotation.
    kit.servo[pin].set_pulse_width_range(500, 2500)
    kit.servo[pin].actuation_range = 270
    kit.servo[pin].angle = degree
    return 1

'''
The way we want this to move is very simple

Attach patch on limb 4 and limb 5 (Gecko is engaged)
Push limb1,limb2,limb3 forward (Motor angle zero)
Attach patch on 1,2,3 now all 5 patches are engaged.
Detach patch 4 and 5. (G-1-2-3)

extend 4 and 5 (M4 and M5 is 0)
simeltainously (If possible) If not extend sepeartely

Now compress limbs 1-2-3 (Motor angle is 100) #Now compress limbs 4 and 5 (Motor angle is 100)
Detach the front Geckos (All patches disengaged)

Also a viable alternative is to suck air out of patch 4 and 5 and get them to neutral
'''

counter = 1

while counter:
    ## Move patch on 4 and 5 to engage
    # function move_patch(pin,step,size)
    move_patch(12,247,0.36)
    move_patch(14,247,0.36)
    ## Push Limbs 1,2,3 (Order will be 3-2-1)
    move_leg(11,20)
    move_leg(9,20)
    move_leg(7,20)
    time.sleep(4)
    # Now attach the 3 patches
    
    move_patch(10,247,0.36)
    time.sleep(1)
    move_patch(8,247,0.36)
    time.sleep(1)
    move_patch(6,247,0.36)
    # Now either compress leg 4 and 5 if that works
    time.sleep(4)
    
    move_leg(13,0)
    move_leg(15,0)
    time.sleep(4)

    move_patch(12,349,0.48)
    move_patch(14,349,0.48)
    time.sleep(2)
    #Revert 1 2 3 to home position

    move_leg(11,100)
    move_leg(7,100)
    time.sleep(2.5)

    move_leg(9,100)
    time.sleep(2.5)

    move_leg(13,140)
    #time.sleep(2.7)
    move_leg(15,140)
    time.sleep(2.7)

    move_patch(10,349,0.40)
    move_patch(8,349,0.42)
    move_patch(6,349,0.42)
    time.sleep(2)
    
    counter -=1
    print(counter)
