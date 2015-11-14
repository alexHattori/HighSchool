#include <AFMotor.h>
#include <VirtualWire.h>

double JoystickVals[2];

AF_DCMotor leftMotor(2);
AF_DCMotor rightMotor(3);
void setup() {
  pinMode(A2,OUTPUT);
  digitalWrite(A2,LOW);
  pinMode(A5, OUTPUT);
  digitalWrite(A5, HIGH);
  vw_set_rx_pin(A3);       
  vw_set_ptt_inverted(true); 
  vw_setup(4000);	     
  vw_rx_start();  
  Serial.begin(9600);  
}

void loop() {
  getVals();
  tankDrive(JoystickVals[0], JoystickVals[1]);
}

//void getVals(){
//  int sensorArray[2];
//  uint8_t buf[VW_MAX_MESSAGE_LEN];
//  uint8_t buflen = VW_MAX_MESSAGE_LEN;
//  if (vw_get_message(buf, &buflen))
//  {
//  for (int i = 0; i < buflen; i++)
//    {
//      sensorArray[i] = buf[i];
//    }
//  JoystickVals[0] = sensorArray[0]/500.0;
//  JoystickVals[1] = sensorArray[1]/500.0;
//  Serial.println(JoystickVals[1]);
//  }
//}
void getVals(){
  uint8_t buf[VW_MAX_MESSAGE_LEN];
  uint8_t buflen = VW_MAX_MESSAGE_LEN;

    int recvData[2]; 
    uint8_t data_size = sizeof(recvData); 

    if (vw_get_message((uint8_t *)&recvData, &data_size)) // Non-blocking
    {
//      Serial.println(recvData[0]);
//      Serial.println(recvData[1]);
      JoystickVals[0] = recvData[0] / 500.0;
      JoystickVals[1] = recvData[1] / 500.0;
	}
   
}
void tankDrive(double stickX, double stickY){
  double leftMotorSpeed;
  double rightMotorSpeed;
     if (stickX >= 0.0) {
       stickX = (stickX * stickX);
           } 
     else {
       stickX = -(stickX * stickX);
           }
     if (stickY >= 0.0) {
       stickY = (stickY * stickY);
           } 
     else {
       stickY = -(stickY * stickY);
           }
    if(abs(stickY) < 0.1){
            leftMotorSpeed = stickX;
            rightMotorSpeed = -stickX;
        }
   if(abs(stickY) < 0.1){
          leftMotorSpeed = stickX;
          rightMotorSpeed = -stickX;
        }
   else if (stickY > 0.0) {
     if (stickX > 0.0) {
       leftMotorSpeed = stickY;
       rightMotorSpeed = stickY * (1-stickX);
     } else {
       leftMotorSpeed = stickY * ( 1 + stickX );
       rightMotorSpeed = stickY;
     }
   } else {
     if (stickX > 0.0) {
       leftMotorSpeed = stickY * (1-stickX);
       rightMotorSpeed = stickY;
     } else {
       leftMotorSpeed = stickY;
       rightMotorSpeed = stickY * (1+stickX);
     }
   }
   runMotors(leftMotorSpeed,rightMotorSpeed);
}
void runMotors(double l, double r){
  int leftSpeed, rightSpeed;
  leftMotor.setSpeed(abs((int)(l*200)));
  rightMotor.setSpeed(abs((int)(r*255)));
  if(l<0){
    leftMotor.run(BACKWARD);
  }
  else{
    leftMotor.run(FORWARD);
  }
  if(r<0){
    rightMotor.run(BACKWARD);
  }
  else{
    rightMotor.run(FORWARD);
  }
}
