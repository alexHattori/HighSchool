void setup() {
  pinMode(9,OUTPUT);
  pinMode(10,INPUT);
  Serial.begin(9600);
}

void loop() {
  long duration;
  digitalWrite(9,HIGH);
  delay(20);
  digitalWrite(9,LOW);
  duration = pulseIn(10, HIGH);

  Serial.println(convertToInches(duration));
  delay(100);
}
long convertToInches(long microseconds){
 return microseconds / 74 / 2; 
}
long covertToCentimeters(long microseconds){
  return microseconds / 29 / 2;
}
