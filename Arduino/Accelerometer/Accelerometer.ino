

void setup() {
  pinMode(A0,OUTPUT);
  pinMode(A4,OUTPUT);

  digitalWrite(A0,LOW);
  digitalWrite(A4,HIGH);

  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(A1));
  Serial.print(" ");
  Serial.print(analogRead(A2));
  Serial.print(" ");
  Serial.println(analogRead(A3));

}

