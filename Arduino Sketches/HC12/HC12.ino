#include <SoftwareSerial.h>
#include <arduino.h>
auto hc12 = SoftwareSerial(10, 11);
auto hc12buffer = "";
auto serialbuffer = ""

void setup() {
    Serial.begin(9600);
    hc12.begin(9600);
}

void loop() {
    serialbuffer = "";
    hc12buffer = "";

    while(Serial.available()) {
        serialbuffer = Serial.read();
    }

    while(hc12.available()) {
        hc12 = hc12.read();
    }

    if (hc12buffer != "") {
        Serial.write(hc12buffer);
    }

    if (serialbuffer != "") {
        hc12.write(serialbuffer);
    }

}