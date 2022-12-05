#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib
import matplotlib.pyplot as plt

# Adjust label positions.
matplotlib.rcParams['xtick.major.pad'] = -1
matplotlib.rcParams['axes.labelpad'] = -5


def get_path(ext, suff=''):
    return os.path.splitext(os.path.basename(
        sys.argv[0]))[0] + suff + '.' + ext


def savefig(fig, suff=''):
    path = get_path('svg', suff)
    print(path)
    fig.savefig(path, metadata={'Date': None})


np.random.seed(2022)
N = 1000
# Points.
xp = np.random.rand(N)
yp = np.random.rand(N)

# Grid.
x1 = np.linspace(0, 1, 100)
y1 = np.linspace(0, 1, 100)
x, y = np.meshgrid(x1, y1)


def f(x, y):
    return np.sin(((1 - x)**2 + (1 - y)**2) ** 0.5 * np.pi * 2)


def monomial(x, y, i, j):
    return x**i * y**j


def f_interp(x, y, c):
    res = np.zeros_like(x)
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            res += c[i, j] * monomial(x, y, i, j)
    return res


# Data in points.
zp = f(xp, yp) + np.random.normal(size=N) * 0.05

deg = (4, 4)
monomials = [
    monomial(xp, yp, i, j) for i in range(deg[0] + 1)
    for j in range(deg[1] + 1)
]
c = np.linalg.lstsq(np.array(monomials).T, zp, rcond=None)[0]
c = c.reshape((deg[0] + 1, deg[1] + 1))

# Values on grid.
zi = f_interp(x, y, c)
zpi = f_interp(xp, yp, c)

def plot_mpl():
    fig, ax = plt.subplots(figsize=(2.5, 2.5),
                           subplot_kw={
                               'projection': '3d',
                               'computed_zorder': False,
                           })
    ax.set_box_aspect((4, 4, 3), zoom=1.1)

    ax.plot_surface(x,
                    y,
                    zi,
                    cmap='jet',
                    edgecolors='k',
                    lw=0.1,
                    alpha=0.8,
                    ccount=25,
                    rcount=25)
    selm = np.where(zp < zpi)
    selp = np.where(zp >= zpi)
    for sel, zorder in [(selm, -1), (selp, 1)]:
        ax.scatter(xp[sel],
                   yp[sel],
                   zp[sel],
                   s=3,
                   c='k',
                   zorder=zorder,
                   edgecolors='none',
                   alpha=1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([0, 0.5, 1])
    savefig(fig)


plot_mpl()
