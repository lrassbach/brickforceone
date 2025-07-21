import basic_mpu
import motorcontroller
import pid
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
        self.y_pid_hover = pid.PID()
        self.y_pid_hover.set_setpoint(0)
        self.x_pid_hover = pid.PID()
        self.x_pid_hover.set_setpoint(0)
        self.acclerometer_x_tolerance = 0.2
        self.acclerometer_y_tolerance = 0.2
        self.acclerometer_z_tolerance = 0 # TODO
        self.command = "maintain"

    def send_command(self):
        self.command =  "maintain" # in future, this will be where commands are received. For now, only command is to hold position
    
    def reset_pids(self):
        pass
        # TODO

    def convert_accel_data_to_action(self, accel_data_i):
        # process x
        x_reading = accel_data_i["x"]
        x_command = self.x_pid_hover.set_process_variable(pv=x_reading)
        x_control = self.x_pid_hover.correction()
        # process y
        y_reading = accel_data_i["y"]
        y_command = self.y_pid_hover.set_process_variable(pv=y_reading)
        y_control = self.y_pid_hover.correction()
        print(x_control, y_control)

    def start(self):
        # self.motor_controller.start()
        self.mpu.collect_bias()
        while True:
            if self.command == "maintain":
                accelerometer_data, gyroscope_data, temperature = self.mpu.read_sensor_data()
                self.convert_accel_data_to_action(accelerometer_data)

if __name__ == "__main__":
    controller = BFOController()
    controller.start()
