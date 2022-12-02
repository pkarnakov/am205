#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import Legendre
from util import get_path, savefig

def f(x):
    return np.sin(-(x + 0.5)**2 * 2) * 0.5 + 1.25

x = np.linspace(-1, 1, 500)

fig, ax = plt.subplots()
ax.set_ylim(0, 2)
ax.plot(x, f(x), c='C0')

n = 6
edges = np.linspace(x.min(), x.max(), n + 1)
for i in range(n):
    x0 = edges[i]
    x1 = edges[i + 1]
    xc = (x0 + x1) * 0.5
    yc = f(xc)
    xx = np.linspace(x0, x1, len(x) // n)
    yy = np.ones_like(xx) * yc
    ax.plot(xx, yy, c='C2')
    ax.plot([x0, x0], [0, yc], c='C2')
    ax.plot([x1, x1], [0, yc], c='C2', clip_on=False)
    ax.scatter(xc, yc, c='k', zorder=5)

ax.set_xlabel('x')
ax.set_ylabel('y')
savefig(fig)
plt.close(fig)
