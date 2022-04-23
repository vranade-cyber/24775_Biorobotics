from __future__ import division
from adafruit_servokit import ServoKit

import time
import Adafruit_PCA9685

motor_deg = self.motor.stall - (self.direction*self.motor.step)
print(motor_deg)
'''
Trial on Motor for limb with 270 degree non_cyclic servo
'''
kit.servo[15].set_pulse_width_range(500, 2500)
kit.servo[15].actuation_range = 270

kit.servo[11].set_pulse_width_range(500, 2500)
kit.servo[11].actuation_range = 180

kit.servo[14].set_pulse_width_range(500, 2500)
kit.servo[14].actuation_range = 120

# Try Variation in Servos.
kit.servo[15].angle = 60
time.sleep(1)

while(1):
    kit.servo[15].angle = 120
    kit.servo[15].angle = 60

    kit.servo[11].angle = 120
    kit.servo[11].angle = 60

    kit.servo[14].angle = 120
    kit.servo[14].angle = 60
