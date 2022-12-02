#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def get_path(ext, suff=''):
    return os.path.splitext(os.path.basename(
        sys.argv[0]))[0] + suff + '.' + ext


def savefig(fig, suff=''):
    path = get_path('svg', suff)
    print(path)
    fig.savefig(path, metadata={'Date': None})

fig, ax = plt.subplots()
x = np.linspace(-1.5, 1.5, 500)
xp = np.linspace(-1, 1, 6)
print(xp)

for i, c, s in [(2, 'C0', 10), (5, 'C1', 5)]:
    yp = np.zeros_like(xp)
    yp[i] = 1
    f = lagrange(xp, yp)
    ax.scatter(xp, yp, c=c, s=s, zorder=10)
    ax.plot(x, f(x), c=c)
ax.axhline(y=0., c='k', ls='--', zorder=-1)
ax.axhline(y=1., c='k', ls='--', zorder=-1)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1., 1.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
savefig(fig)
plt.close(fig)
