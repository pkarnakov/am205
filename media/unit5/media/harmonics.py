#!/usr/bin/env python3
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from util import get_path, savefig

x = np.linspace(0, 1, 500)

for k in range(1, 5):
    fig, ax = plt.subplots(figsize=(1.3, 1.3))
    u = np.sin(np.pi * k * x)
    ax.plot(x, u)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$u$')
    ax.set_ylim(-1.1, 1.1)
    ax.scatter([0, 1], [0, 0], c='k', zorder=5, clip_on=False)
    savefig(fig, suff="_{:}".format(k))
    plt.close(fig)
