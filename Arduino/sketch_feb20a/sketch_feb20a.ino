

const int ledPort = 13;
const int switchPort = 7;

//Accelerometer
const int groundPin = 15;
const int powerPin = 19;
const int zPin = A2;
const int yPin = A3;
const int xPin = A4;

const int xZero = 60;
const int yZero = 85;
const int zZero = 90;

int ledState = LOW;
long previousMillis = 0;
long interval = 100;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPort, OUTPUT);
  pinMode(switchPort, INPUT);
  pinMode(groundPin , OUTPUT);
  pinMode(powerPin , INPUT);
  digitalWrite(groundPin, LOW);
  digitalWrite(powerPin, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  long currentMillis = millis();
  if(currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    ledState++;
    digitalWrite(ledPort, ledState%2);
  }
//  Serial.println(digitalRead(switchPort));
//  Serial.println(analogRead(A0));
  Serial.print(analogRead(xPin));
  Serial.print(",");
  Serial.print(analogRead(yPin));
  Serial.print(",");
  Serial.println(analogRead(zPin));
  delay(100);
}
