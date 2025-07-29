import serial

class MotorController:
  def __init__(self):
    # Set serial port and baud rate
    self.port = '/dev/ttyACM0'
    self.baud_rate = 9600
    self.zero_message = "0,0,0,0" # this will need to be defined as the initial/final message that sets servos to 0
    self.max_speed = 30

  def start(self): 
    # Open the serial port
    self.ser = serial.Serial(self.port, self.baud_rate)
    self.send(self.zero_message)

  def stop(self):
    self.send(self.zero_message)
    self.ser.close()

  def validate_message(self,msg):
    if(msg == "quit"):
      return "quit"
    signal_in = msg.split(",")
    signal_out_arr = []
    len_signal = len(signal_in)
    if(len_signal != 4):
      print(f"BAD COMMAND FORMAT (missing a comma len=={len_signal}); {msg} not sent")
      return None
    try:
      for i in range(4):
        if(int(signal_in[i]) > self.max_speed):
          print(f"CAPPED SPEED at command position: {i}")
          signal_out_arr.append(str(self.max_speed))
        elif(int(signal_in[i]) < 0):
          print(f"NEGATIVE ENCOUNTERED: {i}; {msg} not sent")
          return None
        else:
          signal_out_arr.append(signal_in[i])
      output = ",".join(signal_out_arr)
    except Exception as e:
      print(f"exception: {e}")
      print(f"{msg} not sent")
      return None
    return output

  def send(self, input):
    validated_message = self.validate_message(input)
    if validated_message is not None:
      processed_string = str(validated_message).encode() + b'\n'
      self.ser.write(processed_string)
    else:
      print("No message sent")

if __name__ == "__main__":
  mc = MotorController()
  msg = mc.validate_message("50,0,0,0")
  print(msg)