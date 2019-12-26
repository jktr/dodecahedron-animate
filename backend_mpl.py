import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation as ani

from mpl_toolkits.mplot3d.axes3d import Axes3D

from time import time

def run(animation, N):

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlim3d([-1.0, 1.0]); ax.set_xlabel('X')
    ax.set_ylim3d([-1.0, 1.0]); ax.set_ylabel('Y')
    ax.set_zlim3d([-1.0, 1.0]); ax.set_zlabel('Z')

    def fn(frame):
        ax.collections.clear()
        t = time()
        for seg, _, colors in zip(*frame):
            ax.scatter(*seg, c=colors)
        print('render', (time()-t)*1000)

    a = ani.FuncAnimation(fig, fn, frames=animation, interval=1, blit=False)
    plt.show()
