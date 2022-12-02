#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# Function.
def f(x):
    return np.exp(x) - x - 2


# Exact derivative.
def df(x):
    return np.exp(x) - 1


fig, ax = plt.subplots()
ax.axhline(y=0, lw=0.5, c='k')
xx = np.linspace(1, 2, 500)
ax.plot(xx, f(xx))

# Secant.
xa = 2
xam = xa + 0.1
for i in range(5):
    ax.scatter(xa, f(xa), c='r', zorder=5)
    t = xa - f(xa) * (xa - xam) / (f(xa) - f(xam))
    xam = xa
    xa = t

# Newton.
xb = 2
for i in range(5):
    ax.scatter(xb, f(xb), c='g', zorder=5)
    xb = xb - f(xb) / df(xb)

ax.scatter([], [], c='r', label='secant')
ax.scatter([], [], c='g', label='newton')
ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
fig.savefig("secant_vs_newton.pdf")
