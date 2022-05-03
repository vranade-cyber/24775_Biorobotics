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

move_leg(7,0)   
move_leg(9,0)   
move_leg(11,0)  
move_leg(13,0)  
move_leg(15,0)   
time.sleep(2)

'''
Limb Calibrations:

# Limb 1 29 ml to 14 ml - 15 ml air (sleep timer - 1.4)
# Limb 2 26 ml to 9  ml -  17 ml air (sleep timer - 1.8)
# Limb 3 26 ml to 9  ml - 17 ml air (sleep timer - 1.8)
# Limb 4 26 ml to 12 ml - 14 ml air (sleep timer - 2)
# Limb 5 25 ml to 11 ml - 14 ml air (sleep timer - 2)
'''

counter = 1
while counter:
    move_patch(6,247,0.36)
    move_patch(8,247,0.36)
    time.sleep(2)

    move_patch(6,349,0.48)
    move_patch(8,349,0.48)
    time.sleep(2)
    
    move_patch(10,247,0.36)
    move_patch(10,349,0.48)
    time.sleep(2)
    counter -=1


move_patch(12,247,0.36)
time.sleep(1)

move_patch(10,247,0.34)
time.sleep(1)
move_patch(8,247,0.34)
time.sleep(1)
move_patch(6,247,0.39)
time.sleep(1)
move_patch(14,247,0.36)
time.sleep(3)

#move_patch(12,349,0.36)
#print("Yes")

move_patch(12,349,0.36)
time.sleep(1)
move_patch(10,349,0.34)
time.sleep(1)
move_patch(8,349,0.34)
time.sleep(1)
move_patch(6,349,0.39)
time.sleep(1)
move_patch(14,349,0.36)
time.sleep(1)



'''
Calibratrions
Patch_1 = engage - 247,0.33 Disengage - 349,0.39
Patch_2 = engage - 247,0.33 Disengage - 349,0.33
Patch_3 = engage - 247,0.33 Disengage - 349,0.33
Patch_4 = engage - 247,0.36 Disengage - 349,0.36
Patch_5 = engage - 247,0.36 Disengage - 349,0.36
'''

