int motorPin = 9;

void setup() {
  // put your setup code here, to run once:
  pinMode(motorPin, OUTPUT);
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(motorPin, HIGH);
  digitalWrite(13,LOW);
  delay(1000);
  digitalWrite(motorPin, LOW);
  digitalWrite(13,HIGH);
  delay(1000);
}
