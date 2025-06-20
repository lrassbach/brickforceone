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

    def send_command(self):
        self.command =  "maintain" # in future, this will be where commands are received. For now, only command is to hold position
    
    def start(self):
        self.motor_controller.start()
        self.mpu.collect_bias()
        while True:
            
