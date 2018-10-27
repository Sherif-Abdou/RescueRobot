import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import radians


# Shifts a degree by a certain amount, cycling back to 0 if the new value passes 360
def shift(deg, by):
    new_val = deg+by
    if new_val > 360:
        new_val -= 360
    return new_val


def genFigure(input,lock):
    data = input
    # Initializes Figures
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1,polar=True)
    ax1.set_xticklabels(["E", "NE", "N", "NW", "W", "SW", "S", "SE"])

    # Updates the graph with new data
    def animate(i):
        lock.acquire()
        ax1.clear()
        f = 0
        for mag in data:
            ax1.plot(radians(shift(f, 90)), mag, "bo--")
            f+=1
        lock.release()
        plt.draw()
        plt.pause(0.001)
    # Displays graph
    ani = animation.FuncAnimation(fig, animate, interval=500)
    plt.show()
