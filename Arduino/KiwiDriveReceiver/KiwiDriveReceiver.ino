#include<VirtualWire.h>
#include <SoftwareServo.h>
#include <KiwiDrive.h>

/* 49,50,51,52
 * 53,54,55,56
 * 57,65,66,67
 * 68,69,70,71
 */

SoftwareServo leftServo;
SoftwareServo rightServo;
SoftwareServo frontServo;

int leftSpeeds[] = {0,91,180};//{1300,1525,1700};
int rightSpeeds[] = {0,91,180};//{1300,1525,1700};
int frontSpeeds[] = {0,91,180};//{1300,1525,1700};

double xSpeed;
double ySpeed;
double yaw;

KiwiDrive kw(leftSpeeds,rightSpeeds,frontSpeeds);

void setup() {
  pinMode(5,OUTPUT);
  pinMode(2,OUTPUT);
  digitalWrite(5,LOW);
  digitalWrite(2,HIGH);

  Serial.begin(9600);

  vw_set_rx_pin(3);
  vw_set_ptt_inverted(true); 
  vw_setup(4000);   
  vw_rx_start();

  leftServo.attach(8);
  rightServo.attach(9);
  frontServo.attach(10);

  xSpeed = 0;
  ySpeed = 0;
  yaw = 1;
}

void loop() {
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;
    if (vw_get_message(buf, &buflen))
    {
      int i;
      for (i = 0; i < buflen; i++) {  
        if(buf[i]==50){
          ySpeed+=0.01;   
        }
         }
    }
//    Serial.println(kw.getLeft(xSpeed,ySpeed,yaw));
    leftServo.refresh();
    rightServo.refresh();
    frontServo.refresh();
    leftServo.write(kw.getLeft(xSpeed,ySpeed,yaw));
    rightServo.write(kw.getRight(xSpeed,ySpeed,yaw));
    frontServo.write(kw.getFront(xSpeed,ySpeed,yaw));
}

