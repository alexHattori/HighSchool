#include <VirtualWire.h>

char *controller;

void setup() {
  vw_set_ptt_inverted(true);
  vw_set_tx_pin(7);
  vw_setup(4000);
  
  vw)set_rx_pin(12);
  pinMode(13,OUTPUT);
  
  vw_rx_start();

}

void loop() {
  // put your main code here, to run repeatedly:

}
