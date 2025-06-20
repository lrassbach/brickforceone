import mpu6050
import time

class BasicMPU:
    def __init__(self):
        self.mpu =  mpu6050.mpu6050(0x68)
        self.accel_bias = 0
        self.gyro_bias = 0

    def collect_bias(self):
        time.sleep(5)
        self.accel_bias, self.gyro_bias, temperature = self.read_sensor_data()

    # Define a function to read the sensor data
    def read_sensor_data(self):
        # Read the accelerometer values
        accelerometer_data = self.mpu.get_accel_data()
        accelerometer_data["x"] -= self.accel_bias["x"]
        accelerometer_data["y"] -= self.accel_bias["y"]
        accelerometer_data["z"] -= self.accel_bias["z"]

        # Read the gyroscope values
        gyroscope_data = self.mpu.get_gyro_data()
        gyroscope_data["x"] -= self.gyro_bias["x"]
        gyroscope_data["y"] -= self.gyro_bias["y"]
        gyroscope_data["z"] -= self.gyro_bias["z"]
        # Read temp
        temperature = self.mpu.get_temp()

        return accelerometer_data, gyroscope_data, temperature
    
mpu = BasicMPU()
mpu.collect_bias()
