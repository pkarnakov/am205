#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from util import get_path, savefig

x = np.linspace(0, 2, 500)

def f(x):
    return np.exp(x) - x - 2

fig, ax = plt.subplots()
ax.plot(x, f(x))
ax.axhline(y=0, lw=0.5, c='k', zorder=-5)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_ylim(0, 2)
ax.set_ylim(-1, 3)
savefig(fig)
plt.close(fig)

fig, ax = plt.subplots()
ax.plot(x, f(x))
xk = 1.5
for i in range(5):
    ax.scatter(xk, f(xk), c='C1', zorder=5, s=5, edgecolor='k', lw=0.2)
    xk = np.log(xk + 2)
ax.axhline(y=0, lw=0.5, c='k', zorder=-5)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_ylim(0, 2)
ax.set_ylim(-1, 3)
savefig(fig, suff="_log")
plt.close(fig)

fig, ax = plt.subplots()
ax.plot(x, f(x))
xk = 1.5
for i in range(2):
    ax.scatter(xk, f(xk), c='C1', zorder=5, s=5, edgecolor='k', lw=0.2)
    xk = np.exp(xk) - 2
ax.axhline(y=0, lw=0.5, c='k', zorder=-5)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
savefig(fig, suff="_exp")
plt.close(fig)
