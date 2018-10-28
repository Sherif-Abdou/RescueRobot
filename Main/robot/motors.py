from serial import Serial

class Motors():
    def __init__(self, stepsPerRevolution: int, serial: Serial=None, test_mode=False):
        self.spm = stepsPerRevolution
        self.serial = Serial
        self.test = test_mode
        # Statuses of all four motors, from -1 to 1
        self._m1 = 0
        self._m2 = 0
        self._m3 = 0
        self._m4 = 0
    
    # Returns a tuple with all the motor statuses
    def getMotorSpeeds(self):
        return self._m1, self._m2, self._m3, self._m4

    # Changes the motor speed of a specific motor and updates the arduino with that
    def setMotorSpeed(self, m: int, speed: int):
        if m == 1:
            self._m1 = speed
            self._update(m)
            return self._m1
        elif m == 2:
            self._m2 = speed
            self._update(m)
            return self._m2
        elif m == 3:
            self._m3 = speed
            self._update(m)
            return self._m3
        elif m == 4:
            self._m4 = speed
            self._update(m)
            return self._m4
        else: return
    
    # Sends the packet to change motor speed through seiral connection
    def _update(self, m: int):
        output = "m"+str(m)
        mstr = ""
        if m == 1:
            mstr = self._m1
        elif m == 2:
            mstr = self._m2
        elif m == 3:
            mstr = self._m3
        elif m == 4:
            mstr = self._m4
        output += str(mstr)
        # Doesn't actually use serial port when testing
        if not self.test:
            self.serial.write(output)
        return output
