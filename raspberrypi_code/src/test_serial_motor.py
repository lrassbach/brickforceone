
import motorcontroller


try:
  mc = motorcontroller.MotorController()
  mc.start()
  while True:
    # Get input from the user (example)
    message = input("Enter message to send: ")
    mc.send(message)
    
except KeyboardInterrupt:
    mc.stop()
    print("Serial port closed.")