
#include <Servo.h>

Servo myservo1,myservo2,myservo3;  // create servo object to control a servo
int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin

void setup() {
  Serial.begin(9600);
  myservo1.attach(3);
  myservo2.attach(4);
  myservo3.attach(5);// attaches the servo on pin 9 to the servo object
}\

void loop() {

  myservo1.write(90);                  // sets the servo position according to the scaled value
  delay(5000);  

  myservo2.write(45);
  delay(3000);

  for(int i=0;i<90;i++)
  {
    i=i+5;
    myservo3.write(i);
  }

 myservo2.write(90);
  delay(3000);

  for(int i=0;i<90;i++)
  {
    
    i=i+5;
    myservo3.write(i);
  }
                                     
}

