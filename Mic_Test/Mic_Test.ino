
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(A0, INPUT);
pinMode(A1, INPUT);
pinMode(A2, INPUT);
pinMode(A3, INPUT);
}

void loop() {

 int Mic0 = analogRead(A0);
 int Mic1 = analogRead(A1);
 int Mic2 = analogRead(A2);
 int Mic3 = analogRead(A3);
  
  // put your main code here, to run repeatedly:

Serial.print( Mic0 );
Serial.print(" ");
Serial.print( Mic1 );
Serial.print(" ");
Serial.print( Mic2 );
Serial.print(" ");
Serial.println( Mic3 );
delay(10);
}
