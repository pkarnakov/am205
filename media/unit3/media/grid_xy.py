#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import get_path, savefig


def run(c, suff):
    fig, ax = plt.subplots(figsize=(3, 3))
    nx = 11
    ny = 11

    x = np.linspace(0, 1., nx)
    y = np.linspace(0, 1., ny)
    hx = x[1] - x[0]
    hy = y[1] - y[0]

    xx, yy = np.meshgrid(x, y)
    ax.scatter(xx, yy, clip_on=False, zorder=5, c='k', s=5, edgecolor='none')

    ax.grid(lw=0.5)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(x[0], y[-1])
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_xticks(x, map(lambda q: '{:.2g}'.format(q), x))
    ax.set_yticks(y, map(lambda q: '{:.2g}'.format(q), y))
    ax.set_aspect('equal')
    savefig(fig, suff=suff)
    plt.close(fig)


run(None, suff='')
