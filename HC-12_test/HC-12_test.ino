/*    Arduino Long Range Wireless Communication using HC-12
                      Example 01
   by Dejan Nedelkovski, www.HowToMechatronics.com
*/
#include <SoftwareSerial.h>
SoftwareSerial HC12(10, 11); // HC-12 TX Pin, HC-12 RX Pin
byte incomingByte;
String readBuffer = "";


void setup() {
  Serial.begin(9600);             // Serial port to computer
  HC12.begin(9600);               // Serial port to HC12
 
  
}
void loop() {
  while (HC12.available()) {        // If HC-12 has data
   // Serial.write(HC12.read());      // Send the data to Serial monitor
          readBuffer = HC12.read();
          if(1 = readBuffer){
   Serial.println("daboonhaters");
    }  
  }
  while (Serial.available()) {      // If Serial monitor has data
   // readBuffer = Serial.available();
 //   if(readBuffer = 1){
    HC12.write(Serial.read());      // Send that data to HC-12
    }
    
   // HC12.write(Serial.read());      // Send that data to HC-12
  }
