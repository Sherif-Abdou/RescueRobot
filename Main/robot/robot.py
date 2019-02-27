from serial import Serial
from robot.lights import Lights
from robot.gyro import Gyro, Acceleration, Rotation
from robot.motors import Motors
from robot.lidar import Lidar
from robot.distance import DistanceSensor
from time import sleep
from rplidar import RPLidar
from threading import Thread
from robot.mic import Mic
import zlib
import json


class Robot():
    def __init__(self, serial: Serial,hc: Serial, motor: Serial, lidar: RPLidar=None):
        self.serial = serial
        self.gyro = Gyro()
        self.lights = Lights()
        self.motors = motor
        self.hc = hc
        self.lidar = Lidar()
        self.distance_sensor = DistanceSensor()
        self.rotation = Rotation()
        self.acceleration = Acceleration()
        self.mic = Mic()
        self.parser = Thread(target=self.parseInputs, daemon=True)
        self.sender = Thread(target=self.sendLidarOutput, daemon=True)
        self.parser.start()
        self.sender.start()

    def parseInputs(self):
        while True:
            raw_data = self.serial.readline()
            if raw_data is not None:
                data = raw_data.decode("utf-8")
                if data != "":
                    if data[0] == 'm':
                        print(data)
                        self.motors.write(raw_data) 
                    elif data[0] == 'd':
                        self.distance_sensor.getDistance(data)
                    elif data[0] == 'g':
                        new_data = data.replace("g", "", 1)
                        output = self.gyro.getGyroData(new_data)
                        self.rotation = output[0]
                        self.acceleration = output[1]
                    elif data[0] == 'a':
                        self.mic.parseInput(data)
            hc_data = self.hc.readline()
            data = None
            if hc_data != None:
                data = hc_data.decode("utf-8")
            if data is not None and data != "": 
                print(data)
                self.motors.write(hc_data) 
 

    def sendLidarOutput(self):
        while True:
            data = self.lidar.data
            raw_json = json.dumps(data)
            compressed_json = zlib.compress(raw_json.encode('utf-8'))
            self.hc.write(compressed_json)
            sleep(1)
