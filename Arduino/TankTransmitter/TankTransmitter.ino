#include <VirtualWire.h>

const int xPort = 9;
const int yPort = 8;
void setup() {
  pinMode(11,OUTPUT);
  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);
  digitalWrite(11, LOW);

  pinMode(A4,OUTPUT);
  pinMode(A5,OUTPUT);
  digitalWrite(A4,HIGH);
  digitalWrite(A5,LOW);
  
  vw_set_tx_pin(A3);         
  vw_set_ptt_inverted(true);  
  vw_setup(4000);	 
  Serial.begin(9600);
}

void loop() {
  sendVals();
//  Serial.println(getValue(xPort));
//  Serial.println(getValue(yPort));
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
  Serial.println(val);
  return val;
}
