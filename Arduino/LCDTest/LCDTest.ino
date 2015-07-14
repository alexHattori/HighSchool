#include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,5,4,3,2);
void setup() {

  pinMode(A0,OUTPUT);
  digitalWrite(A0,HIGH);
  
  lcd.begin(16,2);
  lcd.print("hello world!");
}

void loop() {
  

}
