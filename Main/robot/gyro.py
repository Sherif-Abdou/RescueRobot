from serial import Serial

class Acceleration:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

class Rotation:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

class Gyro:
    def __init__(self, serial: Serial=None):
        self.serial = serial

    def getGyroData(self, data=""):
        raw_input = data
        splitted_input = raw_input.split(":")
        accel_data = splitted_input[0]
        rotate_data = splitted_input[1]
        raw_accel = accel_data.split(" ")
        raw_rotate = rotate_data.split(" ")
        accel = Acceleration(x=float(raw_accel[0]), y=float(raw_accel[1]), z=float(raw_accel[2]))
        rotate = Rotation(x=float(raw_rotate[0]), y=float(raw_rotate[1]), z=float(raw_rotate[2]))
        return accel, rotate
