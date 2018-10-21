import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
from math import radians
import threading
lock = threading.Lock()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,polar=True)
data = []
for x in range(360):
    data.append(random.randint(19, 20))

def changeValue():
    time.sleep(1)
    for x in range(360):
        lock.acquire()
        data.append(random.randint(10, 15))
        lock.release()

def animate(i):
    lock.acquire()
    f = 0
    for mag in data:
        ax1.plot(radians(f), mag, "bo--")
        f+=1
    lock.release()
    plt.draw()
    plt.pause(0.001)
def showPlot():
    plt.show()
ani = animation.FuncAnimation(fig, animate, interval=16.66)
thread = threading.Thread(target=changeValue)
thread.start()
plt.show()
