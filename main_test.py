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
        
        
    
    def disengage_gecko(self,motor):
        self.motor = motor
        self.move_servo(self.pinG,1,self.motor)
        return 1
    
    def engage_gecko(self,motor):
        self.motor = motor
        self.move_servo(self.pinG,-1,self.motor)
        return 1
    
    def extend_limb(self,motor):
        self.motor = motor
        self.move_leg(self.pinL,1,self.motor)
        return 1

    def contract_limb(self,motor):
        self.motor = motor
        self.move_leg(self.pinL,0,self.motor)
        return 1
    
    def limb_to_home(self,motor):
        self.motor = motor
        kit.servo[self.pin].set_pulse_width_range(500, 2500)
        kit.servo[self.pin].actuation_range = 270
        #print(self.direction,self.motor.step)
        kit.servo[self.pin].angle = 0
        time.sleep(1)
        
### This Code works for L1 Test.
pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)
kit = ServoKit(channels=16)

M_starfish = motor(180,100,2)
M_gecko = motor(307,60,0.35)

L5 = Limb(15,14,M_starfish,M_gecko)
L4 = Limb(13,12,M_starfish,M_gecko)
L3 = Limb(11,10,M_starfish,M_gecko)
L2 = Limb(9,8,M_starfish,M_gecko)
L1 = Limb(7,6,M_starfish,M_gecko)



counter  = 1
while counter:
    
    
    #L1.extend_limb(M_starfish)
    #L2.extend_limb(M_starfish)
    #L3.extend_limb(M_starfish) #26ml to 9ml: 17ml
    #L4.extend_limb(M_starfish) #22ml to 12ml: 10ml
    #L5.extend_limb(M_starfish) #22 to 12ml: 10ml
    
    #L1.engage_gecko(M_gecko)
    #L2.engage_gecko(M_gecko)   # Gear malfunctioning.
    #L3.engage_gecko(M_gecko)
    #L4.engage_gecko(M_gecko)
    #L5.engage_gecko(M_gecko)

    L1.disengage_gecko(M_gecko)
    L2.disengage_gecko(M_gecko)
    L3.disengage_gecko(M_gecko)
    L4.disengage_gecko(M_gecko)
    L5.disengage_gecko(M_gecko)
    
    #L1.contract_limb(M_starfish)
    #L2.contract_limb(M_starfish)
    #L3.contract_limb(M_starfish) #17ml
    #L4.contract_limb(M_starfish) #10ml
    #L5.contract_limb(M_starfish)

#control strategy
    #L3.engage_gecko(M_gecko)
    '''
    L4.engage_gecko(M_gecko)
    L5.engage_gecko(M_gecko)
    
    
        # Move Forward
    L1.extend_limb(M_starfish)
    L2.extend_limb(M_starfish)
    L3.extend_limb(M_starfish)
    
    L4.extend_limb(M_starfish)
    L5.extend_limb(M_starfish)
    
        # Engage Forward Limbs
    L1.engage_gecko(M_gecko)
    L2.engage_gecko(M_gecko)
    L3.engage_gecko(M_gecko)
        # Disengage Back Limbs
    
    L4.disengage_gecko(M_gecko)
    L5.disengage_gecko(M_gecko)
        
        # Shift Forward -> Compress back Limbs
    
    L4.contract_limb(M_starfish)
    L5.contract_limb(M_starfish)
        
        # Compress Forward Limbs Just for stall
    L1.contract_limb(M_starfish)
    L2.contract_limb(M_starfish)
    L3.contract_limb(M_starfish)
        #Disengage Gecko Patch
    L1.disengage_gecko(M_gecko)
    L2.disengage_gecko(M_gecko)
    L3.disengage_gecko(M_gecko)
    '''
    
    counter -= 1
    #break

#pwm.set_pwm(15,0,0)
def Move_to_target(start,end):
    dist = abs(end - start)
    steps = (dist//1.2) + 1
    print(steps)
    
    while steps:
        
        # Engage Lower Limb
        L3.engage_gecko(M_gecko)
        L4.engage_gecko(M_gecko)
        L5.engage_gecko(M_gecko)
        
        # Move Forward
        L1.extend_limb(M_starfish)
        L2.extend_limb(M_starfish)
        
        # Engage Forward Limbs
        L1.engage_gecko(M_gecko)
        L2.engage_gecko(M_gecko)
        
        # Disengage Back Limbs
        L3.disengage_gecko(M_gecko)
        L4.disengage_gecko(M_gecko)
        L5.disengage_gecko(M_gecko)
        
        # Shift Forward -> Compress back Limbs
        L3.contract_limb(M_starfish)
        L4.contract_limb(M_starfish)
        L5.contract_limb(M_starfish)
        
        # Compress Forward Limbs Just for stall
        L1.contract_limb(M_starfish)
        L2.contract_limb(M_starfish)
        
        #Disengage Gecko Patch
        L1.disengage_gecko(M_gecko)
        L2.disengage_gecko(M_gecko)
        
        if steps%100 == 0:
            print('Steps left',steps-1)
        steps -=1
    
    print('Motion complete')
    return 1
# Add function to get all limb servos to Home
# Home is zero Also change step size 
#Move_to_target(0,6)