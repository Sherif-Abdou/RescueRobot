
class Mic():
    def __init__(self):
        self.amplitude = 0
    
    def parseInput(self, raw_input: str):
        strinput = raw_input.lstrip('a')
        self.amplitude = float(strinput)
        return float(strinput)