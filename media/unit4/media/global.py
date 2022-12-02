#!/usr/bin/env python3
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from util import get_path, savefig

x = np.linspace(-1, 1, 500)

def f(x):
    return 1 + 2 * x ** 2

fig, ax = plt.subplots()
ax.plot(x, f(x))
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_ylim(0, 3)
savefig(fig, suff="_one")
plt.close(fig)


fig, ax = plt.subplots()
ax.plot(x, f(x) + np.sin(x * 50) * 0.2)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_ylim(0, 3)
savefig(fig, suff="_many")
plt.close(fig)
