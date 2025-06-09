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

  // Attach E ESC on pin 8
  starboardESC.attach(8,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  starboardESC.write(starboardPotValue);

  // Attach W ESC on pin 9
  portESC.attach(9,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
  portESC.write(portPotValue);

  Serial.begin(9600);
  // irrecv.enableIRIn();
  // irrecv.blink13(true);
  bowESC.write(bowPotValue);
}

void loop() {
  /*
  if (irrecv.decode()){
      Serial.println(irrecv.decodedIRData.decodedRawData, HEX);
      if(irrecv.decodedIRData.decodedRawData == 0xBF40FF00){
        frontPotValue = 10;
        backPotValue = 16;      
      }
      else if(irrecv.decodedIRData.decodedRawData == 0xF609FF00){
        frontPotValue += 10;
        backPotValue +=10;
      }
      else if(irrecv.decodedIRData.decodedRawData == 0xF807FF00){
        frontPotValue -= 10;
        backPotValue -= 10;
      }
      else if(irrecv.decodedIRData.decodedRawData == 0xBA45FF00){
        frontPotValue = 0;
        backPotValue = 0;
      } 
      else if(irrecv.decodedIRData.decodedRawData == 0xB946FF00){
        frontPotValue++;
        backPotValue++;
      }
      else if(irrecv.decodedIRData.decodedRawData == 0xEA15FF00){
        frontPotValue--;
        backPotValue--;
      }
  //    irrecv.resume();
      Serial.println(frontPotValue);
      Serial.println(backPotValue);
  }*/

  
  

  
}
