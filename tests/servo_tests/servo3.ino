int motor_input1=11;
int motor_input2=10;
int motor_input3=9;
int motor_input4=8;
String voice;

void setup() 
{
  Serial.begin(9600);
  pinMode(motor_input1, OUTPUT);   //RIGHT MOTOR
  pinMode(motor_input2, OUTPUT);   //RIGHT MOTOR
  pinMode(motor_input3, OUTPUT);   //LEFT MOTOR
  pinMode(motor_input4, OUTPUT);   //LEFT MOTOR
}
void loop() 
{  
  while(Serial.available()>0)
  {
    delay(10);
    char c=Serial.read();
    if(c=='#')
    {
      break;
    }
    voice+=c;
    }
   if(voice=="forward"){
    digitalWrite(motor_input1, LOW);
    digitalWrite(motor_input2, HIGH);
    digitalWrite(motor_input3, LOW);
    digitalWrite(motor_input4, HIGH);
     delay(2000);
    }
  else
    if(voice=="back"){
    digitalWrite(motor_input1, HIGH);
    digitalWrite(motor_input2, LOW);
    digitalWrite(motor_input3, HIGH);
    digitalWrite(motor_input4, LOW);  
    delay(2000);}
  else
   if(voice=="right"){
    digitalWrite(motor_input1, LOW);
    digitalWrite(motor_input2, HIGH);
    digitalWrite(motor_input3, HIGH);
    digitalWrite(motor_input4, LOW);
    delay(800); 
    }
  else
   if(voice=="left"){
    digitalWrite(motor_input1, HIGH);
    digitalWrite(motor_input2, LOW);
    digitalWrite(motor_input3, LOW);
    digitalWrite(motor_input4, HIGH);
    delay(800);   }
   if(voice.length()>0)
    {
      Serial.println(voice);
       voice="";
    digitalWrite(motor_input1, LOW);
    digitalWrite(motor_input2, LOW);
    digitalWrite(motor_input3, LOW);
    digitalWrite(motor_input4, LOW);
    }
    }
