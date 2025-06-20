import basic_mpu
import motorcontroller
'''
This module controls the quadcopter.
a) receive readings from mpu6050
b) manage 4 PID for each motor
c) control motors
'''
# TODO set up class; implement for the two motors first

class BFOController:
    def __init__(self):
        self.mpu = basic_mpu.BasicMPU()
        self.motor_controller = motorcontroller.MotorController()