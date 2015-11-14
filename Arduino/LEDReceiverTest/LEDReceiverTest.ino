#include <VirtualWire.h>
double JoystickVals[2];


void setup() {
  pinMode(A2,OUTPUT);
  pinMode(A5,OUTPUT);
  digitalWrite(A2,LOW);
  digitalWrite(A5,HIGH);
  vw_set_rx_pin(A3);       
  vw_set_ptt_inverted(true); 
  vw_setup(4000);	     
  vw_rx_start();      
  Serial.begin(9600);
}

void loop() {
  getVals();
//  Serial.println(JoystickVals[0]);
}

void getVals(){
  uint8_t buf[VW_MAX_MESSAGE_LEN];
  uint8_t buflen = VW_MAX_MESSAGE_LEN;
  if(vw_get_message(buf, &buflen)) // non-blocking I/O
  {
    int i;
    // Message with a good checksum received, dump HEX
    Serial.print("Got: ");
    for(i = 0; i < buflen; ++i)
    {
      Serial.write(buf[i]);
	  //Serial.print(buf[i]);
    }
    Serial.println("");
  }
}
//void getVals(){
//  double sensorArray[2];
//  uint8_t buf[VW_MAX_MESSAGE_LEN];
//  uint8_t buflen = VW_MAX_MESSAGE_LEN;
//  if (vw_get_message(buf, &buflen))
//  {
//  for (int i = 0; i < buflen; i++)
//    {
//      sensorArray[i] = double(buf[i]);
//    }
//  JoystickVals[0] = sensorArray[0];
//  JoystickVals[1] = sensorArray[1];
//  }
//}
