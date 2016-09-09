"""
Visualizing Bubble Sorting.
"""
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    global length, rects, fig, ax
    fig, ax = plt.subplots()

    xpos = np.arange(0, length)
    datalist = range(1, length + 1)
    random.shuffle(datalist)
    ypos = np.asarray(datalist)
    rects = ax.bar(xpos, ypos, alpha=0.4)

def index_gen():
    for i in range(0, (length - 1)):
        for j in range(1, (length - i)):
            yield j

def animate(i):
    if i > 0:
        if rects[i - 1].get_height() > rects[i].get_height():
            tmp = rects[i - 1].get_height()
            rects[i - 1].set_height(rects[i].get_height())
            rects[i].set_height(tmp)

        rects[i - 1].set_color('b')
        rects[i].set_color('y')

    return rects

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        length = int(sys.argv[1])
    else:
        length = 20

    init()
    ani = animation.FuncAnimation(fig, animate, index_gen, repeat=False, blit=True)
    if len(sys.argv) > 2 and sys.argv[2] == 'save':
        ani.save('animation.gif', writer='imagemagick', fps=3)
    else:
        plt.show()
