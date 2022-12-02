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
hx = x1[1] - x1[0]
hy = y1[1] - y1[0]


def run(case='x2y2'):
    fig, ax = plt.subplots(figsize=(3.5, 3.5), subplot_kw={
        'projection': '3d',
    })
    ax.set_box_aspect((4, 4, 3), zoom=1.1)

    zticks = None
    f = None
    pp = None
    cc = [0, 0]
    pp = [(-1 - hx, -1+hy), (-1 - hx, 1-hy), (-1+hx, 1+hy), (1-hx, 1+hy)]
    def pint():
        for i in range(len(pp)):
            p = pp[i]
            pp[i] = (x1[np.argmin(abs(p[0] - x1))], y1[np.argmin(abs(p[1] - y1))])
    if case == 'x2y2':
        pint()
        f = lambda x, y: x**2 + y**2
        zticks = np.linspace(0, 8, 5)
        cc = [1, 1]
    if case == 'x2my2':
        pp = [(-1 - hx, -1+hy), (-1 - hx, 1-hy), (-1+hx, hy*0.5), (1-hx, hy*0.5)]
        pint()
        f = lambda x, y: x**2 - y**2
        zticks = np.linspace(-4, 4, 5)
        cc = [0, 1]
    if case == 'max':
        pp = [(-1 - 3*hx, -1+hy), (-1 - 3*hx, 1.5-hy), (-1+hx, -1+hy), (1-hx, -1+hy)]
        pint()
        f = lambda x, y: np.max([x**2+(y+1)**2, 0*x+1], axis=0)
        cc = [1, 2]

    if pp is not None:
        for i in range(len(pp) // 2):
            pa = pp[2 * i]
            pb = pp[2 * i + 1]
            ppf = np.array([(p[0], p[1], f(*p)) for p in [pa, pb]]).T
            xx = np.linspace(pa[0], pb[0], 100)
            yy = np.linspace(pa[1], pb[1], 100)
            ff = f(xx, yy)
            c = ['C0', 'C1', 'C2'][cc[i]]
            ax.plot(xx, yy, ff, c=c, lw=2, zorder=5)
            ax.plot(ppf[0], ppf[1], ppf[2], c='k', lw=1, zorder=5, marker='o')

    u = f(x, y)
    if case == 'x2y2':
        u[x - y > 3.5] = np.nan

    surf = ax.plot_surface(x,
                           y,
                           u,
                           color='none',
                           rstride=1,
                           cstride=1,
                           linewidth=0.1,
                           edgecolors='k')
    ax.grid(False)
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
run('max')
