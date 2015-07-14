
int ledState = LOW;
long previousMillis = 0;
long interval = 100;

void setup() {
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  
  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);
}

void loop() {
  digitalWrite(12, HIGH);
  delay(100);
  digitalWrite(12, LOW);
  digitalWrite(11, HIGH);
  delay(100);
  digitalWrite(11, LOW);
  digitalWrite(10, HIGH);
  delay(100);
  digitalWrite(10, LOW);
  digitalWrite(7, HIGH);
  delay(100);
  digitalWrite(7, LOW);
  digitalWrite(6, HIGH);
  delay(100);
  digitalWrite(6, LOW);
  digitalWrite(5, HIGH);
  delay(100);
  digitalWrite(5, LOW);
  digitalWrite(6, HIGH);
  delay(100);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  delay(100);
  digitalWrite(7, LOW);
  digitalWrite(10, HIGH);
  delay(100);
  digitalWrite(10, LOW);
  digitalWrite(11, HIGH); 
  delay(100);
  digitalWrite(11, LOW);
  digitalWrite(12, HIGH);
  delay(100);
}
