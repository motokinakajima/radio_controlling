#include <Servo.h>
#define ESC_PIN 6
String message;
long value;
int val;
int input_val;
Servo esc;
void setup(){
  esc.attach(ESC_PIN);
  esc.writeMicroseconds(800);
  delay(2000);
  Serial.begin(9600);
}
void loop(){
  /*
  message = Serial.read();
  value = message.toInt();
  val = (int)value;
  val *= 5;
  val += 800;
  */
  if(Serial.available() > 0){
    message = Serial.read();
    value = message.toInt();
    val = (int)value;
    val *= 5;
    val += 800;
    Serial.println(val);
  }
  esc.writeMicroseconds(val);
}
