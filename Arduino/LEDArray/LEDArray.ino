    int sonar = 7;
    int mode = 6;
    int LEDs [7];
    int dt = 30;
    
    void setup() {
      pinMode(0,INPUT_PULLUP);
      pinMode(10,OUTPUT);
      pinMode(9, OUTPUT);
      pinMode(8,OUTPUT);
      pinMode(7,OUTPUT);
      pinMode(6,OUTPUT);
      pinMode(5,OUTPUT);
      pinMode(4,OUTPUT);
   
      LEDs[0] = 10;
      LEDs[1] = 9;
      LEDs[2] = 8;
      LEDs[3] = 7;
      LEDs[4] = 6;
      LEDs[5] = 5;
      LEDs[6] = 4;
           
      Serial.begin(9600);
    }
    
    void loop() {
      if(digitalRead(0) == LOW){
        if(mode<6){
          mode++;
          clear();
          digitalWrite(LEDs[6-mode], HIGH);
          delay(500);
        }
        else{
          mode = 0;
          digitalWrite(4,HIGH);
          delay(500);
          clear();
        }
        delay(500);
      }
      play(mode);
      
    
    }
    void play(int x){
      if(x == 0){
        for(int i = 0; i < sizeof(LEDs); i++){
          delay(dt);
          clear();
          digitalWrite(i,HIGH);
        }
      }
      else if(x==1) {
        for(int i = 0; i < sizeof(LEDs); i++){
          delay(dt);
          clear();
          digitalWrite(i,HIGH);
        }
        for(int i = sizeof(LEDs); i >=0; i--){
          clear();
          digitalWrite(i,HIGH);
          delay(dt);
        }
        clear();
      }
      else if(x==2){
        clear();
        for(int i = 0; i < sizeof(LEDs); i++){
          delay(dt);
          digitalWrite(i,HIGH);
        }
        delay(dt*2);
        clear();
      }
      else if(x==5){
        clear();
        int count = 0;
        while(count < sizeof(LEDs)){
          int x = random(4,10);
          if(digitalRead(x) == LOW){
          digitalWrite(x,HIGH);
          delay(dt*4);
          count++;
          }
        }
        delay(dt*2);
        clear();
      }
      else if(x==4){
        clear();
        for(int i = 2; i < sizeof(LEDs)/2 + 1; i++){
          digitalWrite(i-2,HIGH);
          delay(dt);
          digitalWrite(i,HIGH);
          delay(dt);
          digitalWrite(sizeof(LEDs)-i,HIGH);
          delay(dt);
        }
        delay(dt*4);
        clear();
      }
      else if(x==3){
        for(int i = 0; i < sizeof(LEDs)-2;i++){
          digitalWrite(i,HIGH);
          digitalWrite(i+3,HIGH);
          delay(dt*2);
          clear();
        } 
        delay(dt);
        clear();
      }
      else if(x==6){
        clear();
      }
    }
    void clear(){
      for(int x = 0; x < sizeof(LEDs); x ++){
        digitalWrite(x,LOW);
      }
    }
    
