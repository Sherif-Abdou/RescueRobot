from rplidar import RPLidar
import threading
import json

class Scan():
    def __init__(self, lidar):
        self.lidar = lidar
        # Stores the 0-359 angle distances to be sent to computer
        self.map = {}

    def scan(self, lock):
        # Constantly scans with the lidar and outputs to the map
        for i, scan in enumerate(self.lidar.iter_scans()):
            if scan[1].is_integer():
                 lock.acquire()
                 self.map[scan[1]] = scan[2]
                 lock.release()

    def jsonOutput(self):
        return json.dumps(self.map)