#include <Keypad.h>
#include <VirtualWire.h>

  const byte ROWS = 4;
  const byte COLS = 4;
  
  char keys[ROWS][COLS] = {
    {'1','2','3','4'},
    {'5','6','7','8'},
    {'9','A','B','C'},
    {'D','E','F','G'}
  };
  
  byte rowPins[ROWS] = {10,9,8,7};
  byte colPins[COLS] = {6,5,4,3};
  
  Keypad kpd = Keypad(makeKeymap(keys),rowPins, colPins, ROWS, COLS);

  
  void setup() {
    pinMode(A4,OUTPUT);
    pinMode(A5,OUTPUT);
    digitalWrite(A4,HIGH);
    digitalWrite(A5,LOW);

    vw_set_tx_pin(A3);         
    vw_set_ptt_inverted(true);  
    vw_setup(4000);  
    Serial.begin(9600);
  }
  void loop() {
    char key[1] = {kpd.getKey()};
    if(key[0] != NO_KEY) {
      Serial.println(key[0]);
      vw_send((uint8_t *)key,1);
      vw_wait_tx();
    }
  }
