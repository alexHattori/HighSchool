#include <VirtualWire.h>

int xport = A4;
int yport = A5;
void setup() {
  pinMode(A1,OUTPUT);
  pinMode(A2, OUTPUT);
  digitalWrite(A1, HIGH);
  digitalWrite(A2, LOW);
  vw_set_tx_pin(A0);         
  vw_set_ptt_inverted(true);  
  vw_setup(4000);	 
}

void loop() {
  sendVals();
}

void sendVals(){
  const char *msg = "Hello";
//  double JoystickVals[2];
//  JoystickVals[0] = getValue(xport);
//  JoystickVals[1] = getValue(yport);
//  vw_send((uint8_t *)JoystickVals, sizeof(JoystickVals));
//  vw_wait_tx();
//  delay(100);
  vw_send((uint8_t *)msg, strlen(msg));
  delay(50);
}
double getValue(int port){
  double val = analogRead(port)-500;
  if(val > 500){
    val = 500;
  }
  if(abs(val) <= 50){
    val = 0;
  }
  return  val / 500;
}
