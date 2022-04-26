from __future__ import division
from adafruit_servokit import ServoKit
import time
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
    def __init__(self,pinL,pinG,motor1,motor2):
        ## Motor gives the stall values and so on
        ## pinL is Pin to move servo forward
        ## pinG is Pin to engage and disengage the gecko Patch->(Engage by 1, disengage -1)
        #self.motor = motor
        self.pinL = pinL
        self.pinG = pinG
        self.sleep_time1 = motor1.time # can also use motor.time
        self.sleep_time2 = motor2.time
        
    def move_servo(self,pin,direction,motor):
        #Base function can be used for Gecko Engage,Disengage,Limb extention and contraction
        self.motor = motor
        pwm_val = self.motor.stall + direction*self.motor.step
        pwm.set_pwm(pin, 0, pwm_val)
        
        print('Test Fn',pwm_val)
        
        #Send some PWM input to servo to make it move
        time.sleep(self.motor.time)
        # Hold that torque
        
        pwm.set_pwm(pin,0,self.motor.stall)
        time.sleep(1)
        
        print('Loop broken')
        
        return 0
    def move_leg(self,pin,direction,motor):
        self.pin = pin
        self.motor = motor
        self.direction = direction
        
        motor_deg = self.motor.stall - (self.direction*self.motor.step)
        print(motor_deg)
        
        kit.servo[self.pin].set_pulse_width_range(500, 2500)
        kit.servo[self.pin].actuation_range = 270
        #print(self.direction,self.motor.step)
        kit.servo[self.pin].angle = motor_deg
        time.sleep(self.motor.time)
        
        
    
    def engage_gecko(self,motor):
        self.motor = motor
        self.move_servo(self.pinG,1,self.motor)
        return 1
    
    def disengage_gecko(self,motor):
        self.motor = motor
        self.move_servo(self.pinG,-1,self.motor)
        return 1
    
    def extend_limb(self,motor):
        self.motor = motor
        self.move_leg(self.pinL,-1,self.motor)
        return 1
    
    def contract_limb(self,motor):
        self.motor = motor
        self.move_leg(self.pinL,0,self.motor)
        return 1
### This Code works for L1 Test.
pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)
kit = ServoKit(channels=16)

M_starfish = motor(180,80,2)
M_gecko = motor(307,102,0.18)

L1 = Limb(15,14,M_starfish,M_gecko) # Test Motors with Gecko Pins - 14,12,10,8,6
L2 = Limb(13,12,M_starfish,M_gecko)
L3 = Limb(11,10,M_starfish,M_gecko)
L4 = Limb(9,8,M_starfish,M_gecko)
L5 = Limb(7,6,M_starfish,M_gecko)

counter = 5

while  counter:
    L1.engage_gecko(M_gecko)
    L2.engage_gecko(M_gecko)
    L3.engage_gecko(M_gecko)
    L4.engage_gecko(M_gecko)
    L5.engage_gecko(M_gecko)

    L1.disengage_gecko(M_gecko)
    L2.disengage_gecko(M_gecko)
    L3.disengage_gecko(M_gecko)
    L4.disengage_gecko(M_gecko)
    L5.disengage_gecko(M_gecko)
    counter -=1