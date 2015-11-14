#include <Servo.h>

Servo rightDrive;
Servo leftDrive;
Servo frontDrive;

int speed = 1300;

void setup() {
  Serial.begin(9600);
  rightDrive.attach(9);
  leftDrive.attach(8);
  frontDrive.attach(10);
  
  rightDrive.writeMicroseconds(1500);
  leftDrive.writeMicroseconds(1525);
  frontDrive.writeMicroseconds(1525);
}

void loop() {
//speed+=10;
//Serial.println(speed);
//rightDrive.writeMicroseconds(speed);
//delay(1000);
}

//servo.writeMicroseconds(1500);     //stop
//
//servo.writeMicroseconds(1300);     //turn right
//
//servo.writeMicroseconds(1700);     //turn left
