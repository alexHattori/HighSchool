  #include <Keypad.h>
  
  const byte ROWS = 4;
  const byte COLS = 4;
  
  char keys[ROWS][COLS] = {
    {'1','2','3','4'},
    {'5','6','7','8'},
    {'9','A','B','C'},
    {'D','E','F','G'}
  };
  
  byte rowPins[ROWS] = {4,5,6,7};
  byte colPins[COLS] = {10,11,12,13};
  
  Keypad kpd = Keypad(makeKeymap(keys),rowPins, colPins, ROWS, COLS);
  void setup() {
    Serial.begin(9600);
  }
  void loop() {
  char key = kpd.getKey();
  if(key != NO_KEY) {
    Serial.println(key);
  }
  }
