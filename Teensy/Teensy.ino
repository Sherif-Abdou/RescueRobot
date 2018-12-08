#include <SoftwareSerial.h>
#include <TeensyThreads.h>

struct ServoPins {
	int mainpin;
	int in1;
	int in2;
};

auto x = 0;
int lightPins[] = {2, 3};
int hc12rx = 0;
int hc12tx = 1;


ServoPins servopins[3];
// SoftwareSerial HC12(hc12rx, hc12tx);

void parseCommand(String commandd) {
	int number;
	switch (commandd[0]) {
	case 'm':
		Serial.println("motor change");
		number = ((int)commandd[1] - 48)-1;
		switch(commandd[2]) {
		case '+':
			// analogWrite(servopins[number].mainpin, 30);
			// digialWrite(servopins[number].in1, LOW);
			// digialWrite(servopins[number].in2, HIGH);
			Serial.println("Forward");
			break;
		case '-':
			// analogWrite(servopins[number].mainpin, 30);
			// digialWrite(servopins[number].in1, HIGH);
			// digialWrite(servopins[number].in2, LOW);
			Serial.println("Backward");
			break;
		case '0':
			// analogWrite(servopins[number].mainpin, 0);
			Serial.println("Stop");
			break;
		default: break;
		}
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
		default: break;
		}
		break;
	}
}

void messages(SoftwareSerial& hc12) {
	while (true) {
		if (hc12.available()) {
			auto readbuffer = hc12.read();
			Serial.write(readbuffer);
		}
	}
}

void test(int counter) {
	while (true) {
		counter++;
		Serial.println(counter);
		delay(100);
	}
}

void setup() {
	Serial.begin(115200);
//  for (auto i = 0; i < 4; i++) {
//    servos[i].attach(servoPins[i])
//  }
	// threads.addThread(messages, HC12);
	threads.addThread(test, x);
}

void loop() {
	parseCommand("m3+");
	delay(3000);
	parseCommand("l2-");
	delay(10000);
}
