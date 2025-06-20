import serial

# Set serial port and baud rate
serial_port = '/dev/ttyACM0'  # Or /dev/ttyUSB0, etc.
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

try:
  while True:
    # Get input from the user (example)
    message = input("Enter message to send: ")
    if(message == "quit"):
        ser.write(str("0,0,0,0").encode() + b'\n') 
        ser.close()
        print("Serial port closed.")
        quit()
    
    # Encode the message and send it to the Arduino
    ser.write(message.encode() + b'\n') 
    print("Sent:", message)
    
except KeyboardInterrupt:
    ser.write(str("0,0,0,0") + b'\n') 
    ser.close()
    print("Serial port closed.")