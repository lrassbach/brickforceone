import basic_mpu
import motorcontroller
import pid
import random
'''
This module controls the quadcopter.
a) receive readings from mpu6050
b) manage 2 PID for x,y axis
c) control motors

/*
bow: front (WASHINGTON)
stern: back (11)
port: left (434)
starboard: right (YA)
*/
'''
# TODO set up class; implement for the two motors first

class BFOController:
    def __init__(self):
        self.mpu = basic_mpu.BasicMPU()
        self.motor_controller = motorcontroller.MotorController()
        self.y_pid_accel = pid.PID()
        self.y_pid_accel.set_setpoint(0)
        self.x_pid_accel = pid.PID()
        self.x_pid_accel.set_setpoint(0)
        self.y_pid_gyro = pid.PID()
        self.y_pid_gyro.set_setpoint(0)
        self.x_pid_gyro = pid.PID()
        self.x_pid_gyro.set_setpoint(0)
        self.acclerometer_x_tolerance = 0.2
        self.acclerometer_y_tolerance = 0.2
        self.acclerometer_z_tolerance = 0 # TODO
        self.command = "maintain"

    def send_command(self):
        self.command =  "maintain" # in future, this will be where commands are received. For now, only command is to hold position
    
    def reset_pids(self):
        pass
        # TODO

    def convert_raw_data_to_action(self, accel_data_i, gyro_data_i):
        # process x accel
        x_reading_accel = accel_data_i["x"]
        self.x_pid_accel.set_process_variable(pv=x_reading_accel)
        x_control_accel = self.x_pid_accel.correction()
        # process x gyro
        x_reading_gyro = gyro_data_i["x"]
        self.x_pid_gyro.set_process_variable(pv=x_reading_gyro)
        x_control_gyro = self.x_pid_gyro.correction()
        # process y accel
        y_reading_accel = accel_data_i["y"]
        self.y_pid_accel.set_process_variable(pv=y_reading_accel)
        y_control_accel = self.y_pid_accel.correction()
        # process y gyro
        y_reading_gyro = gyro_data_i["y"]
        self.y_pid_gyro.set_process_variable(pv=y_reading_gyro)
        y_control_gyro = self.y_pid_gyro.correction()

        """
        pid action :: options to correct :: state
        /*
        In order to prevent favoring an action that is equivalent, i.e. increasing in a certain direction
        vs. decreasing in the opposite, the action is chosen with uniform probability. Over the long run the
        options will be chosen equally as often, hopefully preventing any favoring and minimizing upward or 
        downward drift.

        Actions are mapped to a dict with the increment required to match new the state 
        int[Bow,Stern,Starboard,Port]
        */
        ___________________
        x+y+ ::  (decrease starboard || increase port) && (increase bow || decrease stern)
        y+x- :: (increase bow || decrease stern) && (increase starboard || decrease port)
        x-y- :: (increase starboard || decrease port) && (decrease bow || increase stern)
        y-x+ :: (decrease bow || increase stern) && (decrease starboard || increase port)
        y+ ::  (increase bow || decrease stern)
        x- :: (increase starboard || decrease port)
        y- :: (decrease bow || increase stern)
        x+ :: (decrease starboard || increase port)
        """
        action = None
        state = None
        random_choice = random()
        if(y_control_accel > self.acclerometer_y_tolerance and x_control_accel > self.acclerometer_x_tolerance): # x+y+
            state = "x+y+"
            if random_choice < 0.5: # left side of or
                action = [1,0,-1,0]
            else: # right side of or
                action = [0,-1,0,1]
        elif(y_control_accel > self.acclerometer_y_tolerance and x_control_accel < -1*self.acclerometer_x_tolerance): #y+x-
            state = "y+x-"
            if random_choice < 0.5: # left side of or
                action = [1,0,1,0]
            else: # right side of or
                action = [0,-1,0,-1]
        elif(y_control_accel < -1*self.acclerometer_y_tolerance and x_control_accel < -1*self.acclerometer_x_tolerance): #x-y-
            state = "x-y-"
            if random_choice < 0.5: # left side of or
                action = [-1,0,1,0]
            else: # right side of or
                action = [0,1,0,-1]
        elif(y_control_accel <  -1*self.acclerometer_y_tolerance and x_control_accel > self.acclerometer_x_tolerance): #y-x+
            state = "y-x+"
            if random_choice < 0.5: # left side of or
                action = [-1,0,-1,0]
            else: # right side of or
                action = [0,1,0,1]
        elif(y_control_accel > self.acclerometer_y_tolerance): #y+
            state = "y+"
            if random_choice < 0.5: # left side of or
                action = [1,0,0,0]
            else: # right side of or
                action = [0,-1,0,0]
        elif(x_control_accel < -1*self.acclerometer_x_tolerance): #x-
            state = "x-"
            if random_choice < 0.5: # left side of or
                action = [0,0,1,0]
            else: # right side of or
                action = [0,0,0,-1]
        elif(y_control_accel < -1*self.acclerometer_y_tolerance): #y-
            state = "y-"
            if random_choice < 0.5: # left side of or
                action = [-1,0,0,0]
            else: # right side of or
                action = [0,1,0,0]
        elif(x_control_accel > self.acclerometer_x_tolerance): #x+
            state = "x+"
            if random_choice < 0.5: # left side of or
                action = [0,0,-1,0]
            else: # right side of or
                action = [0,0,0,1]
        else:
            state = "maintain"
            action = [0,0,0,0]
        return state, action

    def start(self):
        # self.motor_controller.start()
        self.mpu.collect_bias()
        while True:
            if self.command == "maintain":
                accelerometer_data, gyroscope_data, temperature = self.mpu.read_sensor_data()
                state, action = self.convert_raw_data_to_action(accelerometer_data,gyroscope_data)

if __name__ == "__main__":
    controller = BFOController()
    controller.start()
