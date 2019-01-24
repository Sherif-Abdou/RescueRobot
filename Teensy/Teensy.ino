#include <DFRobot_VL53L0X.h>
#include <Adafruit_LSM9DS1.h>
#include <TeensyThreads.h>
#include <SoftwareSerial.h>
#include <Wire.h>

// Sensors
DFRobotVL53L0X distance_sensor;
Adafruit_LSM9DS1 gyro = Adafruit_LSM9DS1();
const int mic[3] {A9, A8, A1};

// Sensor data
sensors_event_t accel, mag, rot, temp;
volatile double distance;
volatile double amp[3] {0.0, 0.0, 0.0};


// Collects sensor data
void sensor_collection() {
  while (true) {
    gyro.getEvent(&accel, &mag, &rot, &temp);
    distance = distance_sensor.getDistance();
  }
}

void mic_collection(int micnum) {
  while (true) {
    unsigned int sample;
    unsigned long startMillis = millis(); // Start of sample window
    unsigned int peakToPeak = 0;   // peak-to-peak level

    unsigned int signalMax = 0;
    unsigned int signalMin = 1024;

    // collect data for 50 mS
    while (millis() - startMillis < 50)
    {
      sample = analogRead(mic[micnum]);
      if (sample < 1024)
      {
        if (sample > signalMax)
        {
          signalMax = sample;
        }
        else if (sample < signalMin)
        {
          signalMin = sample;
        }
      }
    }
    amp[micnum] = (signalMax + signalMin)/2;
  }
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  // Set I2C sub-device address
  distance_sensor.begin(0x50);
  // Sensor Config
  distance_sensor.setMode(Continuous, High);
  gyro.setupAccel(gyro.LSM9DS1_ACCELRANGE_2G);
  gyro.setupMag(gyro.LSM9DS1_MAGGAIN_4GAUSS);
  gyro.setupGyro(gyro.LSM9DS1_GYROSCALE_245DPS);
  // Starting the Sensor
  distance_sensor.start();
  gyro.begin();
  // Starting Background Threads
  threads.addThread(sensor_collection);
  threads.addThread(mic_collection, 0);
  threads.addThread(mic_collection, 1);
  threads.addThread(mic_collection, 2);
}

void loop() {
  Serial.println("d" + String(distance));
  Serial.println("g"+String(accel.acceleration.x)+" "+String(accel.acceleration.y)+" "+String(accel.acceleration.z)+":"+String(rot.gyro.x)+" "+String(rot.gyro.y)+" "+ String(rot.gyro.z));
  Serial.println("a" + String(amp[0]));
  delay(1000);
}
