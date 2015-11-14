#include <SoftwareServo.h>
#include <KiwiDrive.h>

SoftwareServo leftServo;
SoftwareServo rightServo;
SoftwareServo frontServo;

int leftSpeeds[] = {0,90,180};
int rightSpeeds[] = {0,90,180};
int frontSpeeds[] = {0,90,180};
KiwiDrive kw(leftSpeeds,rightSpeeds,frontSpeeds);
void setup() {
  Serial.begin(9600);
  leftServo.attach(8);
  rightServo.attach(9);
  frontServo.attach(10);
}

void loop() {
  leftServo.write(kw.getLeft(0,0,11.625));
  rightServo.write(kw.getRight(0,0,11.625));
  frontServo.write(kw.getFront(0,0,11.625));

}
