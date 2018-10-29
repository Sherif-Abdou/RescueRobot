from threading import Thread
from serial import Serial

class DistanceSensor():
    def __init__(self, serial: Serial=None):
        self.serial = serial
        self.distance = None

    def getDistance(self):
        if self.serial is not None:
            raw_data = self.serial.readline()
            if raw_data[0] == "d":
                raw_data = raw_data.lstrip("d")
                return float(raw_data)
