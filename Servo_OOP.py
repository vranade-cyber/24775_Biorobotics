from __future__ import division
import time
#import servo
# Import the PCA9685 module.
import Adafruit_PCA9685

class motor:
    def __init__(self, stall, step , time):
        ## The Stall is calibrated stall torque for the given motor.
        ## The step is the addition or subtraction taken with step moving it CW or CCW
        self.stall = stall
        self.step = step
        self.time = time
    
    def motor_move(self):
        # This is a  dummy function for future use left blank
        print('Yes Motor checks')
        return 1
    

class Limb:
    def __init__(self,pinL,pinG,motor , direction):
        ## Motor gives the stall values and so on
        ## pinL is Pin to move servo forward
        ## pinG is Pin to engage and disengage the gecko Patch->(Engage by 1, disengage -1)
        self.motor = motor
        self.pinL = pinL
        self.pinG = pinG
        self.sleep_time = self.motor.time # can also use motor.time
        self.direction = direction
    def move_servo(self,pin,direction):
        #Base function can be used for Gecko Engage,Disengage,Limb extention and contraction
        
        print('Test Fn')
        
        counter = 1
        
        while counter:
            counter -=1
            #Break Loop
            pwm.set_pwm(pin, 0, self.motor.stall + self.direction*self.motor.step)
            #Send some PWM input to servo to make it move
            time.sleep(self.sleep_time)
            # Hold that torque
            pwm.set_pwm(pin,0,self.motor.stall)
            time.sleep(1)
            ## Stall Servo
            #break
        print('Loop broken')
        
        return 0

### This Code works for L1 Test.
pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)
M1 = motor(307,102,0.18)
M1.motor_move()
L1 = Limb(0,15,M1,1)
#L2 = Limb(0,15,M1,1)
counter  = 5
while counter:
    
    L1.move_servo(0,1)
    L1.move_servo(15,-1)
    
    print('Both work')
    counter -=1

pwm.set_pwm(15,0,0)
time.sleep(1)

            
            
        