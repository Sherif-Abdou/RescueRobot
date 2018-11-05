from rplidar import RPLidar
from threading import Thread

class Lidar:
    def __init__(self, lidar: RPLidar=None):
        self.lidar = lidar
        self.data = []
        for _ in range(360):
            self.data.append(None)
        self.updater = Thread(target=self.updateMeasures)


    def updateMeasures(self):
        for scan in self.lidar.iter_scans():
            if float(scan[1]).is_integer():
                self.data[int(scan[1])] = scan[2]
