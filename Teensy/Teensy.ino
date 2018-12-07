#include <Servo.h>

auto x = 0;
int servoPins[] = {12, 13, 14, 15};
int lightPins[] = {2, 3};
Servo servos[4];

void parseCommand(String commandd) {
  int number;
  switch (commandd[0]) {
  case 'm':
    Serial.println("motor change");
    number = (int)commandd[1] - 48;
    Serial.println(number);
    break;
  case 'l':
    Serial.println("light signal");
    number = (int)commandd[1] - 48;
    Serial.println(number);
    switch(commandd[2]) {
      case '+':
//        digitalWrite(lightPins[number-1], LOW);
          Serial.println(HIGH);
      case '-':
//        digitalWrite(ligthPins[number-1], HIGH);
          Serial.println(LOW);
    }
    break;
  }
}

void setup() {
  Serial.begin(9600);
//  for (auto i = 0; i < 4; i++) {
//    servos[i].attach(servoPins[i])
//  }
  
}

void loop() {
    parseCommand("m3+");
    delay(3000);
    parseCommand("l2-");
    delay(10000);
}
