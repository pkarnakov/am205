#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import get_path, savefig
from scipy.interpolate import lagrange

fig, ax = plt.subplots()
x = np.linspace(-1.5, 1.5, 500)
n = 15
xp = np.linspace(-1, 1, n)

for i, c, s in [(5, 'C0', 10), (10, 'C1', 5)]:
    yp = np.zeros_like(xp)
    yp[i] = 1
    f = lagrange(xp, yp)
    ax.scatter(xp, yp, c=c, s=s, zorder=10)
    ax.plot(x, f(x), c=c, label=r"$L_{{{:}}}$".format(i))
ax.set_title(r"$n={:}$".format(n), pad=-20)

ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-50, 50)
ax.set_yticks([-50, -25, 0, 25, 50])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
savefig(fig)
plt.close(fig)
