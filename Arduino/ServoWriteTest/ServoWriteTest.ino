#include <SoftwareServo.h>

SoftwareServo testServo;
int angle = -10;
void setup() {
  testServo.attach(8);
  Serial.begin(9600);
}

void loop() {
  Serial.println(angle);
  testServo.writeMicroseconds(angle);
  angle+=1;

}
