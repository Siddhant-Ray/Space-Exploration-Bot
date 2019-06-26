

int sensor_pin0 = A0;
int sensor_pin1 = A1;
int sensor_pin2 = A2;



int output_value0;
int output_value1;
int output_value2;

void setup() {

   Serial.begin(9600);

   Serial.println("Reading From the Sensor ...");

   delay(2000);

  

   }

void loop() {

   output_value0= analogRead(sensor_pin0);

   output_value0 = map(output_value0,550,0,0,100);

   Serial.print("Mositure : ");

   Serial.print(output_value0);

   Serial.println("%");
  
   delay(5000);


   output_value1= analogRead(sensor_pin1);

   

   Serial.print("Gas level: ");

   Serial.print(output_value1);

   Serial.println();

   delay(5000);


   output_value2= analogRead(sensor_pin2);

   

   Serial.print("Temperature : ");

   Serial.print(output_value2/46);

   Serial.println();

   delay(5000);
  
   
   }
