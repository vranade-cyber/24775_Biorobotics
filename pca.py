from __future__ import division
import time
#import servo
# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)


def Myfunc(counter):
    if counter == 5:
        print('Function call works')
    
    return 0

def move_limb(pin,direction):
    counter = 5
    while counter:
        
        pwm.set_pwm(pin, 0, stall + direction*102)
        time.sleep(0.2)
        print('Control Ran')
        
        pwm.set_pwm(pin,0,stall)
    
        counter -= 1

    print('Loop ends')
    
    
def move_patch(pin,direction):
    counter = 5
    while counter:
        
        pwm.set_pwm(pin, 0, stall + direction*102)
        time.sleep(0.2)
        print('Control Ran')
        
        pwm.set_pwm(pin,0,stall)
    
        counter -= 1

    print('Loop ends')
    
        
servo_min = 150  # Min pulse length out of 4096
servo_max = 600
servo_disp = 250
stall = 307
counter = 1

'''
while counter:
    pwm.set_pwm(15, 0, 205)
    time.sleep(0.18)
    print('Condition CW triggered')
    
    pwm.set_pwm(15, 0 ,stall)
    time.sleep(1)
    
    pwm.set_pwm(15, 0, 409)
    time.sleep(0.19)
    print('Condition CCW triggered')
    
    pwm.set_pwm(15, 0 ,307)
    time.sleep(1)

    counter -=1
    if counter%10==0:
        print(counter)
    Myfunc(counter) 
    
    break
'''
counter = 10
while counter:
    pwm.set_pwm(15, 0, 205) # max Anticlockwise
    time.sleep(1)

    print('Stall trigger')
    pwm.set_pwm(15, 0 , 215) # max Stall
    time.sleep(1)
    #pwm.set_pwm(15, 0, 257) # max Clockwise
    time.sleep(0.5)

    
    counter-=1
    
    pwm.set_pwm(15, 0, 0)
    time.sleep(1)


