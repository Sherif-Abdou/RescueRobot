from serial import Serial
from robot.lights import Lights
from robot.gyro import Gyro, Acceleration, Rotation
from robot.motors import Motors
from robot.lidar import Lidar
from robot.distance import DistanceSensor
from time import sleep
import zlib
import json


class Robot():
    def __init__(self, serial: Serial):
        self.serial = serial
        self.gyro = Gyro()
        self.lights = Lights()
        self.motors = Motors()
        self.lidar = Lidar()
        self.distance_sensor = DistanceSensor()
        self.rotation = Rotation()
        self.acceleration = Acceleration()

    def parseInputs(self):
        while True:
            raw_data = self.serial.read_all()
            if raw_data is not None:
                data = raw_data.decode("utf-8")
                if data[0] == 'm':
                    pass
                elif data[0] == 'd':
                    self.distance_sensor.getDistance(data)
                elif data[0] == 'g':
                    new_data = data.replace("g", "", 1)
                    output = self.gyro.getGyroData(new_data)
                    self.rotation = output[0]
                    self.acceleration = output[1]
                self.serial.reset_input_buffer()

    def sendLidarOutput(self):
        while True:
            data = self.lidar.data
            raw_json = json.dumps(data)
            compressed_json = zlib.compress(raw_json.encode('utf-8'))
            self.serial.write(compressed_json)
            sleep(1)
