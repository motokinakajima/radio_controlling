#include <Servo.h>
#define ESC_PIN 6
#define LADDER_PIN 5
char input[10];
int i;
int volume = 0;
int volume2 = 90;
String data = "";
bool a = false;
Servo ladder;
Servo esc;
void setup(){
  Serial.begin(115200);
  Serial.println("Start in 2 seconds!!");
  esc.attach(ESC_PIN);
  ladder.attach(LADDER_PIN);
  volume = 800;
  esc.writeMicroseconds(volume);
}

void loop(){
  if (Serial.available()) {
    input[i] = Serial.read();
    if (input[i] == '.') {
      input[i] = '\0';
      //Serial.write(input);
      //Serial.write("\n");
      //Serial.println(data);
      if(data[0] == '1'){
        data.replace("1<","");
        data.replace(">","");
        volume = data.toInt();
        volume *= 6;
        volume += 800;
        if(volume<=820){
          volume = 800;
        }else if(volume>=2050){
          volume = 2250;
        }else{
          volume += 200;
        }
        Serial.println(volume);
        esc.writeMicroseconds(volume);
      }else if(data[0] == '2'){
        data.replace("2<","");
        data.replace(">","");
        volume2 = data.toInt();
        volume2 += 90;
        ladder.write(volume2);
        Serial.println(volume2);
      }
      data = "";
      i = 0;
    }
    else { i++;data += input[i]; }
  }
}
