#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# Function.
def f(x):
    return np.exp(x) - x - 2


fig, ax = plt.subplots()
ax.axhline(y=0, lw=0.5, c='k')
xx = np.linspace(0, 2, 500)
ax.plot(xx, f(xx))

xa = 0.5
for i in range(5):
    ax.scatter(xa, f(xa), c='r', zorder=5)
    xa = np.log(xa + 2)

xb = 1.15
for i in range(5):
    ax.scatter(xb, f(xb), c='g', zorder=5)
    xb = np.exp(xb) - 2

ax.scatter([], [], c='r', label='log')
ax.scatter([], [], c='g', label='exp')
ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
fig.savefig("fixed_point.pdf")
