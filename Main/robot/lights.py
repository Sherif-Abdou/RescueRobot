import sentry_sdk
sentry_sdk.init("https://1e9819f95a3d46fdb1ef8c96287c29e8@sentry.io/1310445")
from serial import Serial
# The class responsible for handling the robot's lights
class Lights():
    def __init__(self, light_serial: Serial=None, test_mode=False):
        self._l1 = False
        self._l2 = False
        self.test = test_mode
        self.serial = light_serial

    # Returns a tuple with the status of both lights
    def getLights(self):
        return self._l1, self._l2

    # Sets one of the lights to a new status
    def setLight(self, l: int, value: bool):
        if l == 1:
            self._l1 = value
            self._update(l)
            return self._l1
        elif l == 2:
            self._l2 = value
            self._update(l)
            return self._l2
        else:
            return
    # Sends any updates to an arduino
    def _update(self, i: int):
        if not self.test:
            output = "l"
            output += i
            if i == 1:
                if self._l1:
                    output+="+"
                elif not self._l1:
                    output+="-"
            elif i == 2:
                if self._l2:
                    output+="+"
                elif not self._l2:
                    output+="-"
            self.serial.write(output)
