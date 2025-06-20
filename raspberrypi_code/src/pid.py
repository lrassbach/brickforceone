import time
import numpy as np

# simple PID. math taken from https://www.digikey.com/en/maker/tutorials/2024/implementing-a-pid-controller-algorithm-in-python

class PID:
    def __init__(self, initial_process_variable=0, k_proportional=1.0, k_integral=0.1,k_derivative=0.05, timestep=0.1):
        self.name = "PID"
        self.setpoint = None # setpoint is the desired state
        self.previous_error = 0
        self.dt = timestep # time step
        self.integral = 0
        self.process_variable = initial_process_variable
        self.k_proportional = k_proportional
        self.k_integral = k_integral
        self.k_derivative = k_derivative

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def set_process_variable(self, pv):
        self.process_variable = pv

    def correction(self):
        error = self.setpoint - self.process_variable
        self.integral += error * self.dt
        derivative = (error - self.previous_error) / self.dt
        control = self.k_proportional * error + self.k_integral * self.integral + self.k_derivative * derivative
        self.previous_error = error
        return control
        
    def get_process_variable(self):
        return self.process_variable
    

def test():
    # intitialize
    pid = PID()
    setpoint = 10 # desired state, typically hold position (neutral). Set by controller module
    pid.set_setpoint(setpoint)
    pid.set_process_variable(0)
    # begin simulation loop
    for i in range(1000):
        # every ten iterations take a new "reading" from a sensor, simulate noise
        if(i % 10 == 0 or i ==0):
            rand_process_var = np.random.randn() + 10
            pid.set_process_variable(pv=rand_process_var)
        control = pid.correction()
        # simulation of sending the correction of  to the output and receiving a new sensor reading
        updated_sensor_reading = pid.get_process_variable() + (control * pid.dt)
        pid.set_process_variable(updated_sensor_reading)
        print(f"setpoint={setpoint}; process variable={pid.process_variable};control={control};iteration={i}")
        # time.sleep(1)

test()