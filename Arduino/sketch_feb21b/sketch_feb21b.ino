int brightness = 0;

void setup() {
 pinMode(11, OUTPUT);
 }

void loop() {
  digitalWrite(11,HIGH);
  brightness++;
  
  delay(100);
}
