import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from math import radians


def shift(deg, by):
    newVal = deg+by
    if newVal > 360:
        newVal -= 360
    return newVal

def genFigure(input,lock):
    data = input
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1,polar=True)

    def animate(i):
        lock.acquire()
        ax1.clear()
        f = 0
        for mag in data:
            ax1.plot(radians(shift(f, 90)), mag, "bo--")
            f+=1
        lock.release()
        ax1.set_xticklabels(["E", "NE", "N", "NW", "W", "SW", "S", "SE"])
        plt.draw()
        plt.pause(0.001)

    ani = animation.FuncAnimation(fig, animate, interval=500)
    plt.show()
