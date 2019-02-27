from rplidar import RPLidar
from threading import Thread
from math import floor

class Lidar:
    def __init__(self, lidar: RPLidar=None):
        self.lidar = lidar
        self.data = []
        for _ in range(360):
            self.data.append(None)
        self.updater = Thread(target=self.updateMeasures)
        self.updater.start()

    def updateMeasures(self):
        if self.lidar != None:
            for _, _, angle, measure in self.lidar.iter_measurments():
                self.data[floor(angle)] = measure
