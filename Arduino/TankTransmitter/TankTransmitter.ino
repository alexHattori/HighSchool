#include <VirtualWire.h>

const int xPort = A1;
const int yPort = A0;
void setup() {
  pinMode(A4,OUTPUT);
  pinMode(A5, OUTPUT);
  digitalWrite(A4, HIGH);
  digitalWrite(A5, LOW);
  vw_set_tx_pin(A3);         
  vw_set_ptt_inverted(true);  
  vw_setup(4000);	 
  Serial.begin(9600);
}

void loop() {
  sendVals();
  
}

void sendVals(){
  int JoystickVals[2];
  JoystickVals[0] = getValue(xPort);
  JoystickVals[1] = getValue(yPort);
  vw_send((uint8_t *)&JoystickVals, sizeof(JoystickVals));
//  vw_send((uint8_t *)getValue(xPort), 3);
  vw_wait_tx();
  delay(50);
}
int getValue(int port){
  double val = analogRead(port)-500;
  if(val > 500){
    val = 500;
  }
  if(abs(val) <= 50){
    val = 0;
  }
  return val;
}
