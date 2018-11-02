class Acceleration:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

class Rotation:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

class Gyro:
    def __init__(self, serial=None):
        self.serial = serial

    def getGyroData(self):
       pass
