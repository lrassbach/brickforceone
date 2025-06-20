import serial

class MotorController:
  def __init__(self):
    # Set serial port and baud rate
    self.port = '/dev/ttyACM0'
    self.baud_rate = 9600
    self.zero_message = "" # this will need to be defined as the initial/final message that sets servos to 0

  def start(self): 
    # Open the serial port
    self.ser = serial.Serial(self.port, self.baud_rate)
    self.ser.write(self.zero_message)

  def stop(self):
    self.ser.write(self.zero_message)
    self.ser.close()

  def send(self, input):
    #  TODO define how messages will be sent and processed. json in? delimited list in a string out?
    processed_string = str(input).encode() + b'\n'
    self.ser.write()

  # TODO this logic needs to be added outside of the class by the caller
  #except Exception:
  #    ser.write(str(0) + b'\n')
  #    ser.close()
  #    print("Serial port closed.")