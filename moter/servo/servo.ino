#include <Servo.h>
#define LADDER_PIN 5
char input[10];
int i;
int volume = 0;
int volume2 = 90;
String data = "";
bool a = false;
Servo ladder;
void setup(){
  Serial.begin(115200);
  ladder.attach(LADDER_PIN);
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
