#include <Servo.h>
#include <KiwiDrive.h>

Servo leftServo;
Servo rightServo;
Servo frontServo;

int leftSpeeds[] = {1300,1525,1700};
int rightSpeeds[] = {1300,1525,1700};
int frontSpeeds[] = {1300,1525,1700};

double xSpeed;
double ySpeed;
double yaw;
KiwiDrive kw(leftSpeeds,rightSpeeds,frontSpeeds);

void setup() {
  leftServo.attach(8);
  rightServo.attach(9);
  frontServo.attach(10);

  xSpeed = 0;
  ySpeed = 0;
  yaw = 0;

}

void loop() {
    xSpeed = 0;
    ySpeed = 0;
    yaw = 0;
    leftServo.writeMicroseconds(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.writeMicroseconds(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.writeMicroseconds(kw.getFront(xSpeed,ySpeed,yaw));
    delay(5000);
    xSpeed = 0;
    ySpeed = 1;
    yaw = 0;
    leftServo.writeMicroseconds(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.writeMicroseconds(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.writeMicroseconds(kw.getFront(xSpeed,ySpeed,yaw));
    delay(5000);
    xSpeed = 0;
    ySpeed = -1;
    yaw = 0;
    leftServo.writeMicroseconds(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.writeMicroseconds(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.writeMicroseconds(kw.getFront(xSpeed,ySpeed,yaw));
    delay(5000);
    xSpeed = 1;
    ySpeed = 0;
    yaw = 0;
    leftServo.writeMicroseconds(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.writeMicroseconds(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.writeMicroseconds(kw.getFront(xSpeed,ySpeed,yaw));
    delay(5000);
    xSpeed = -1;
    ySpeed = 0;
    yaw = 0;
    leftServo.writeMicroseconds(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.writeMicroseconds(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.writeMicroseconds(kw.getFront(xSpeed,ySpeed,yaw));
    delay(5000);
    xSpeed = 0;
    ySpeed = 0;
    yaw =11.625;
    leftServo.writeMicroseconds(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.writeMicroseconds(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.writeMicroseconds(kw.getFront(xSpeed,ySpeed,yaw));
    delay(5000);
    xSpeed = 0;
    ySpeed = 0;
    yaw = -11.625;
    leftServo.writeMicroseconds(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.writeMicroseconds(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.writeMicroseconds(kw.getFront(xSpeed,ySpeed,yaw));
    delay(5000);
}
