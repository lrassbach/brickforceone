#include <Servo.h>
//#include <IRremote.h>

/*
bow: front (WASHINGTON)
stern: back (11)
port: left (434)
starboard: right (YA)
*/

Servo bowESC;
Servo sternESC;
Servo portESC;
Servo starboardESC;
int bowPotValue; // (value between 0 and 180)
int sternPotValue;
int portPotValue;
int starboardPotValue;

const int RECV_PIN_IR = 5;
//IRrecv irrecv(RECV_PIN_IR);

void setup() {
  bowPotValue = 0; // (value between 0 and 180)
  sternPotValue = 0;
  portPotValue = 0;
  starboardPotValue = 0;

  // Attach bow ESC on pin 10
  bowESC.attach(10,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  bowESC.write(bowPotValue);

  // Attach stern ESC on pin 7
  sternESC.attach(7,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  sternESC.write(sternPotValue);

  // Attach starboard ESC on pin 8
  starboardESC.attach(8,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  starboardESC.write(starboardPotValue);

  // Attach port ESC on pin 9
  portESC.attach(9,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  portESC.write(portPotValue);

  Serial.begin(9600);
  // irrecv.enableIRIn();
  // irrecv.blink13(true);
  bowESC.write(bowPotValue);
}

/*
incoming commands will be formatted as
"Bow,Stern,Starboard,Port\n"
newline will be dropped by serial read function
output will be int[Bow,Stern,Starboard,Port]
*/

int* processIncomingMotorCommand(String in){
  int * out = new int[4];
  String current = "";
  int index = 0;
  for(int i = 0; i < in.length(); i++){
    if(in[i] == ','){
      out[index] = current.toInt();
      current = "";
    }
    else if (i == in.length()-1)
    {
      current = current + in[i];
      out[index] = current.toInt();
      current = "";
    }
    else {
      current = current + in[i];
    }
  }
  return out;
}

void loop() {
  if (Serial.available() > 0) {
	  String incomingData = Serial.readStringUntil('\n');
	  int * commands = processIncomingMotorCommand(incomingData);
	  bowPotValue = commands[0];
	  bowESC.write(newSpeed);
    delete commands;
  }
}
