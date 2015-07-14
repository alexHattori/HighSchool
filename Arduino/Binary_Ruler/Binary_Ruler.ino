int LEDs[7];

void setup() {
  pinMode(1,INPUT_PULLUP);
  pinMode(3, OUTPUT);
  pinMode(2, INPUT);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  LEDs[0] = 12;
  LEDs[1] = 11;
  LEDs[2] = 10;
  LEDs[3] = 9;
  LEDs[4] = 8;
  LEDs[5] = 7;
  LEDs[6] = 6;
  Serial.begin(9600);
}

void loop() {

  if(digitalRead(1) == LOW){
    clear();
    Serial.println(getDistance());
    displayDistance((int)(getDistance()));
  }
}

long getDistance(){
  long duration;
  digitalWrite(3,HIGH);
  delay(20);
  digitalWrite(3,LOW);
  duration = pulseIn(2, HIGH);
  
  return duration / 74 / 2; 
}
void displayDistance(int x){
  for(int i = 7; i >= 0; i--){
    if(x>=pow(2,i)){
      digitalWrite(LEDs[i],HIGH);
      x-=pow(2,i);
    }
  }
}
void clear(){
  for(int x = 0; x < sizeof(LEDs); x ++){
        digitalWrite(x,LOW);
      }
}
