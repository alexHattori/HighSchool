#include <AFMotor.h>

AF_DCMotor motor1(3);
AF_DCMotor motor2(2);


void setup(){
  motor1.setSpeed(255);
  motor2.setSpeed(255);
  
  motor1.run(FORWARD);
  motor2.run(FORWARD);
}

void loop(){
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
//  delay(1000);
//  motor1.run(FORWARD);
//  motor2.run(FORWARD);
//  delay(1000);
//  if(getDistanceInches()<12){
//    motor1.run(BACKWARD);
//  }
//  else{
//    motor1.run(FORWARD);
//  }
}
long getDistanceInches(){
  long duration;
  digitalWrite(18,HIGH);
  delay(20);
  digitalWrite(18,LOW);
  duration = pulseIn(19, HIGH);

  return duration / 29 / 2;
}
