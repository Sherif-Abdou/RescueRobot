from serial import Serial
from robot.lights import Lights
from robot.gyro import Gyro, Acceleration, Rotation
from robot.motors import Motors
from robot.lidar import Lidar

class Robot():
    def __init__(self, serial):
        self.serial = serial
        self.gyro = Gyro()
        self.lights = Lights()
        self.motors = Motors()
        self.lidar = Lidar()

