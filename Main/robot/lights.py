from serial import Serial
# The class responsible for handling the robot's lights
class Lights():
    def __init__(self, light_serial: Serial):
        self._l1 = False
        self._l2 = False
        self.serial = light_serial

    def getLights(self):
        return self._l1, self._l2

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
    def _update(self, i: int):
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
