import mpu6050
import time

class BasicMPU:
    def __init__(self):
        self.mpu =  mpu6050.mpu6050(0x68)

    def collect_bias(self):
        time.sleep(5)
        accel_bias, gyro_bias, temperature = self.read_sensor_data()
        print(accel_bias)
        print(gyro_bias)

    # Define a function to read the sensor data
    def read_sensor_data():
        # Read the accelerometer values
        accelerometer_data = mpu6050.get_accel_data()

        # Read the gyroscope values
        gyroscope_data = mpu6050.get_gyro_data()

        # Read temp
        temperature = mpu6050.get_temp()

        return accelerometer_data, gyroscope_data, temperature
    
mpu = BasicMPU()
mpu.collect_bias()