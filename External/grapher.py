import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import radians

plt.switch_backend("QT5Agg")
# Shifts a degree by a certain amount, cycling back to 0 if the new value passes 360
def shift(deg, by):
    new_val = deg+by
    if new_val > 360:
        new_val -= 360
    return new_val

def reflect(deg):
    deg_shift = abs(180-deg)
    if deg < 180:
        return 180+deg_shift
    else:
        return 180-deg_shift

def genFigure(input,lock):
    data = input
    ymax = 10
    # Initializes Figures
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1,polar=True)
    # Updates the graph with new data
    def animate(i):
        # lock.acquire()
        ax1.clear()
        ax1.set_xticklabels(["E", "NE", "N", "NW", "W", "SW", "S", "SE"])
        ax1.set_ylim(0, ymax)
        f = 0
        for mag in data:
            if mag <= ymax:
                ax1.plot(radians(shift(reflect(f), 90)), mag, "k.")
            f+=1
        # lock.release()
    # Displays graph
    ani = animation.FuncAnimation(fig, animate, interval=1)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
