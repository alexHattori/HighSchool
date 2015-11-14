const int xPort = 10;
const int yPort = 11;
//const int zPort = 8;
//const int LED = 13;

void setup() {
//    pinMode(zPort, INPUT);
//    pinMode(LED, OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
//  pinMode(xPort,INPUT);
//  pinMode(yPort,INPUT);
    Serial.begin(9600);
}

void loop() {
  Serial.print("X Value: ");
  Serial.print(getValue(xPort));
  Serial.print(" Y Value: ");
  Serial.println(getValue(yPort));
  
//  if(digitalRead(zPort) == LOW){
//    digitalWrite(LED,HIGH);
//  }
//  else{
//    digitalWrite(LED,LOW);
//  }

}

double getValue(int port){
  double val = analogRead(port)-500;
  if(val > 500){
    val = 500;
  }
  if(abs(val) <= 50){
    val = 0;
  }
  return val / 500;
}
