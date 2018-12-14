import grapher
from threading import Lock, Thread
from time import sleep
import urllib.parse
import urllib.request
from json import loads

data = [0 for _ in range(360)]
url = "http://192.168.86.170:3000/lidar"
def change(data):
    while True:
        raw_input = urllib.request.urlopen(url)
        json_data = raw_input.read().decode('utf-8')
        new_data = loads(json_data)
        # print(json)
        i = 0
        for _ in data:
            data[i] = new_data[i]
            i+=1
        sleep(0.01)

lock = Lock()
thread = Thread(target=change, args=(data,))
thread.start()
grapher.genFigure(data, lock)