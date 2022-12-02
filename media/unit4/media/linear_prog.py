#!/usr/bin/env python3
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from util import get_path, savefig

# ax+b
lines = [
    (0.5, 1),
    (-0.25, 0.75),
    (-1, 1),
]

def line(x, l):
    return l[0] * x + l[1]

def f(x):
    res = np.min([line(x, l) for l in lines], axis=0)
    return res

x = np.linspace(-2, 2, 500)
fig, ax = plt.subplots(figsize=(2.5, 2.5))
for l in lines:
    ax.plot(x, l[0] * x + l[1])
ax.fill_between(x, f(x), y2=-10, facecolor='C6', edgecolor='none')

ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xticks(range(-2, 3))
ax.set_yticks(range(-2, 3))
ax.set_aspect('equal')
savefig(fig)
plt.close(fig)
