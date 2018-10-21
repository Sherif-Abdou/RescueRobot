import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
from math import radians
import threading
import os
lock = threading.Lock()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,polar=True)
data = []
for x in range(360):
    data.append(random.randint(19, 20))

def changeValue():
    time.sleep(4)
    while True:
        for x in range(360):
                lock.acquire()
                data[x] = random.randint(0, 20)
                lock.release()
        time.sleep(1)

def animate(i):
    lock.acquire()
    ax1.clear()
    f = 0
    for mag in data:
        ax1.plot(radians(f), mag, "bo--")
        f+=1
    lock.release()
    ax1.set_xticklabels(['N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE'])
    plt.draw()
    plt.pause(0.001)
def showPlot():
    plt.show()

ani = animation.FuncAnimation(fig, animate, interval=500)
thread = threading.Thread(target=changeValue)
thread.start()
plt.show()
