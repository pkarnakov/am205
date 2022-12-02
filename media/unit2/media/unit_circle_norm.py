#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path

x1 = np.linspace(-1.1, 1.1, 200)
y1 = x1

x, y = np.meshgrid(x1, y1)

for p in [1, 2, 4, 'inf']:
    fig, ax = plt.subplots(figsize=(1.3,1.3))
    if p == 'inf':
        norm = np.maximum(abs(x), abs(y))
    else:
        norm = (abs(x) ** p + abs(y) ** p) ** (1 / p)
    ax.contour(x1, y1, norm, levels=[1.], colors='C0')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_aspect('equal')
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    #ax.axvline(x=0, lw=0.5, ls='-', c='k', zorder=-5)
    #ax.axhline(y=0, lw=0.5, ls='-', c='k', zorder=-5)
    suff = "_{:}".format(p)
    savefig(fig, suff=suff)
    plt.close(fig)
