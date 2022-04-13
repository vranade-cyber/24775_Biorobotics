from __future__ import division
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
    def __init__(self,pinL,pinG,motor , direction):
        ## Motor gives the stall values and so on
        ## pinL is Pin to move servo forward
        ## pinG is Pin to engage and disengage the gecko Patch->(Engage by 1, disengage -1)
        self.motor = motor
        self.pinL = pinL
        self.pinG = pinG
        self.sleep_time = self.motor.time # can also use motor.time
        self.direction = direction
        self.time = time
    def move_servo(self,pin,direction,time):
        #Base function can be used for Gecko Engage,Disengage,Limb extention and contraction
        
        print('Test Fn')
        
        counter = 1
        
        while counter:
            counter -=1
            #Break Loop
            pwm.set_pwm(pin, 0, self.motor.stall + self.direction*self.motor.step)
            #Send some PWM input to servo to make it move
            time.sleep(self.sleep_time)
            # Hold that torque/ May be changed and added to while loop of main/Open loop
            pwm.set_pwm(pin,0,self.motor.stall)
            time.sleep(time)
            ## Stall Servo
            #break
        print('Loop broken')
        
        return 0
    
    def engage_gecko(self):
        move_servo(self.pinG,1,1)
        return 1
    
    def disengage_gecko(self):
        move_servo(self.pinG,-1,1)
        return 1
    
    def extend_limb(self):
        move_servo(self.pinL,1,1)
        return 1
    
    def contract_limb(self):
        move_servo(self.pinL,-1,1)
        return 1

### This Code works for L1 Test.
pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)
M1 = motor(307,102,0.18)
M1.motor_move()

### Initialize Motors
#L1 = Limb(0,1,M1,1)
#L2 = Limb(2,3,M1,1)
#L3 = Limb(4,5,M1,1)
#L4 = Limb(6,7,M1,1)
#L5 = Limb(8,9,M1,1)

'''
Above Way is a very tedious way of doing so.
A way could be to make a dict and add Limbs as Dict Objects with keys being L1,L2,L3 and so on
Also a cool way
'''

'''
c = input('Enter Number of Limbs')
limbs = {}
for i in range(1,int(c)+1):
    limbs[f'L{i}'] = Limb((2*i)-2,(2*i)-1,M1,1)

print(limbs)
'''

def Move_to_target(start,end):
    dist = abs(end - start)
    steps = (dist//1.2) + 1
    print(steps)
    
    while steps:
        
        # Engage Lower Limb
        L3.engage_gecko()
        L4.engage_gecko()
        L5.engage_gecko()
        
        # Move Forward
        L1.extend_limb()
        L2.extend_limb()
        
        # Engage Forward Limbs
        L1.engage_gecko()
        L2.engage_gecko()
        
        # Disengage Back Limbs
        L3.disengage_gecko()
        L4.disengage_gecko()
        L5.disengage_gecko()
        
        # Shift Forward -> Compress back Limbs
        L3.contract_limb()
        L4.contract_limb()
        L5.contract_limb()
        
        # Compress Forward Limbs Just for stall
        L1.contract_limb()
        L2.contract_limb()
        
        #Disengage Gecko Patch
        L1.disengage_gecko()
        L2.disengage_gecko()
        
        if steps%100 == 0:
            print('Steps left',steps-1)
        steps -=1
    
    print('Motion complete')

Move_to_target(0,12)