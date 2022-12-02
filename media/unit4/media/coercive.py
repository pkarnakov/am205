#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.sparse
from util import savefig

# Adjust label positions.
matplotlib.rcParams['xtick.major.pad'] = -1
matplotlib.rcParams['axes.labelpad'] = -5

# Grid size.
nx = 24
ny = nx

xlim = [-2, 2]
ylim = [-2, 2]

x1 = np.linspace(*xlim, nx)
y1 = np.linspace(*ylim, ny)
x, y = np.meshgrid(x1, y1)


def run(case='x2y2'):
    fig, ax = plt.subplots(figsize=(3.5, 3.5),
                           subplot_kw={
                               'projection': '3d',
                           })
    ax.set_box_aspect((4, 4, 3), zoom=1.1)

    zticks = None
    f = None
    if case == 'x2y2':
        f = lambda x, y: x**2 + y**2
        zticks = np.linspace(0, 8, 5)
    if case == 'x2my2':
        f = lambda x, y: x**2 - y**2
        zticks = np.linspace(-4, 4, 5)
    if case == 'exp':
        f = lambda x, y: 1-np.exp(-(x**2 + y**2))
        zticks = np.linspace(0, 1, 3)

    u = f(x, y)
    surf = ax.plot_surface(x,
                           y,
                           u,
                           cmap='jet',
                           rstride=1,
                           cstride=1,
                           linewidth=0.1,
                           edgecolors='k')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f')
    ax.set_xticks(np.linspace(*xlim, 5))
    ax.set_yticks(np.linspace(*ylim, 5))
    if zticks is not None:
        ax.set_zticks(zticks)
    savefig(fig, suff='_' + case, bbox_inches='tight')
    plt.close(fig)


run('x2y2')
run('x2my2')
run('exp')
