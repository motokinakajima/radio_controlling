#include <Servo.h>
#define LADDER_PIN 5
#define MOTER_PIN 3
Servo moter;
Servo ladder;
char input;
int i = 0;
int volume = 0;
int volume2 = 90;
String data = "";
bool a = false;
void setup(){
  Serial.begin(115200);
  moter.attach(MOTER_PIN,800,2300);
  ladder.attach(LADDER_PIN,500,2400);
}
void loop(){
  if (Serial.available()) {
    input = Serial.read();
    if (input == '.') {
      Serial.println(data);
      input = '\0';
      if(data[1] == '1'){
        data.trim();
        data.replace("\n","");
        data.replace("!1<","");
        data.replace(">","");
        volume = data.toInt();
        volume *= 6;
        volume += 800;
        if(volume >= 2200){
          volume = 2200;
        }
        moter.write(volume);
      }else if(data[1] == '2'){
        data.trim();
        data.replace("\n","");
        data.replace("!2<","");
        data.replace(">","");
        volume2 = data.toInt();
        volume2 += 90;
        ladder.write(volume2);
      }
      input=NAN;
      data = "";
      i = 0;
    }
    else {if(input!='\n'){data += input;}}
    /*
    String input_data = Serial.readString();
    Serial.println(input_data);
    if(input_data[0] == '!'){
      Serial.println("sent");
      if(input_data[1] == '1'){
        input_data.replace("1<","");
        input_data.replace(">.","");
        volume = data.toInt();
        Serial.println(volume);
        volume *= 6;
        volume += 800;
        moter.write(volume);
        Serial.println(volume);
      }else if(input_data[1] == '2'){
        input_data.replace("2<","");
        input_data.replace(">.","");
        volume = data.toInt();
        volume += 90;
        ladder.write(volume);
        Serial.println(volume);
      }
    }
    */
  }
}
