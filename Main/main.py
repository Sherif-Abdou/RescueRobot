from serial import Serial
from rplidar import RPLidar
from robot.robot import Robot

lidar = RPLidar("/dev/ttyUSB0")
serial = Serial("/dev/ttyUSB1")

robot = Robot(serial, lidar)

