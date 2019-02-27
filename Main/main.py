#!/usr/bin/env python3
from serial import Serial
from rplidar import RPLidar
from robot.robot import Robot
from time import sleep

lidar = RPLidar("/dev/ttyUSB0")
serial = Serial("/dev/ttyACM0", 9600, timeout=1)
hc = Serial("/dev/ttyUSB1", 9600, timeout=1)
motors = Serial("/dev/ttyUSB2", 9600, timeout=1)
robot = Robot(serial, hc, motors, lidar)
while True:
    print("Distance: %s" % robot.distance_sensor.distance)
    print("Acceleration: %s, %s, %s" % (robot.acceleration.x, robot.acceleration.y, robot.acceleration.z))
    sleep(1)
