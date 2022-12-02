#!/usr/bin/env python3
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from util import get_path, savefig

# Function to consider.
def f(x):
    return x * x - 4 * np.sin(x)


# Initial interval, assume f(a)*f(b)<0.
a = 1
b = 3
tol = 1e-3

x = np.linspace(a, b, 500)
fig, ax = plt.subplots(figsize=(2.8, 1.2))
ax.plot(x, f(x))

# Bisection search
i = 0
dy = 0.7
while b - a > tol:
    c = 0.5 * (b + a)
    ax.scatter(c, f(c), c='k', zorder=5, s=1)
    y = 10 - (i + 1) * dy
    ax.add_patch(
        Rectangle((a, y), b - a, dy, facecolor='C1', lw=0.1, edgecolor='k'))
    #ax.plot([a,b], [y,y], lw=4, alpha=0.5, c='C1')
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    i += 1

c = (a + b) / 2
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=c, ls='--', c='k', lw=0.5, zorder=-5)
ax.axhline(y=0, ls='--', c='k', lw=0.5, zorder=-5)
savefig(fig)
plt.close(fig)
