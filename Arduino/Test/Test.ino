#include<VirtualWire.h>
void setup() {
  pinMode(5,OUTPUT);
  pinMode(2,OUTPUT);
  digitalWrite(5,LOW);
  digitalWrite(2,HIGH);

  Serial.begin(9600);

  vw_set_rx_pin(3);
  vw_set_ptt_inverted(true); 
  vw_setup(4000);   
  vw_rx_start();
}

void loop() {
 uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;
    
    if (vw_get_message(buf, &buflen))
    {
      Serial.println("Hey");
      int i;
      for (i = 0; i < buflen; i++) {  
        Serial.println(buf[i]);   
         }
    }
}
