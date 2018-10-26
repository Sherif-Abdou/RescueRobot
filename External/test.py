import grapher
from threading import Lock, Thread
from time import sleep
data = []
for x in range(360):
    data.append(x/10)
def change(data):
    sleep(3)
    while True:
        i = 0
        for val in data:
            data[int(i)] = val+1
            i+=1
            sleep(0.01)
lock = Lock()
thread = Thread(target=change, args=(data,))
thread.start()
grapher.genFigure(data, lock)