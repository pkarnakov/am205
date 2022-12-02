#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import get_path, savefig


def run(c, suff, arr=False, both=False, noscat=False):
    fig, ax = plt.subplots(figsize=(4, 2))
    nx = 9
    ny = 5

    #x = np.linspace(0, nx - 1, nx)
    #y = np.linspace(0, ny - 1, ny)
    x = np.linspace(0, 1.6, nx)
    y = np.linspace(0, 0.8, ny)
    hx = x[1] - x[0]
    hy = y[1] - y[0]

    xx, yy = np.meshgrid(x, y)
    #ax.scatter(xx, yy, clip_on=False, zorder=5, c='k', s=3, edgecolor='none')

    def point(i, j):
        ax.scatter(x[i],
                   y[j],
                   clip_on=False,
                   zorder=6,
                   facecolor='k',
                   s=13,
                   edgecolor='k',
                   lw=0.25)
    if not noscat:
        i0, j0 = 5, ny - 2
        for i in range(nx):
            for j in range(ny):
                if both:
                    if j <= j0 and (abs(i0 - i) <= j0 - j):
                        point(i, j)
                else:
                    if j <= j0 and (i <= i0 and i0 - i <= j0 - j):
                        point(i, j)
        ax.text(x[i0] + hx * 0.05, y[j0] + hy * 0.2, r"$U_j^{n+1}$")

        dy = y[j0] - y[0]
        if c is None:
            pass
        elif both:
            ax.plot([x[i0], x[i0] - c * dy], [y[j0], y[j0] - dy], c='k')
            ax.plot([x[i0], x[i0] + c * dy], [y[j0], y[j0] - dy], c='k')
        else:
            ax.plot([x[i0], x[i0] - c * dy], [y[j0], y[j0] - dy], c='k')

    def arrow(xy, dxy, c):
        xy = np.array(xy)
        dxy = np.array(dxy)
        for q in [-1, 1]:
            ax.arrow(
                *(xy + dxy * 0.5),
                *(dxy * q * 0.5) * 0.95,
                color=c,
                overhang=0.2,
                head_width=lw * 7,
                head_length=lw * 10,
                length_includes_head=True,
                zorder=8,
            )

    if arr:
        lw = 0.003
        arrow((x[i0], y[j0 - 1]), (-hx * c, 0), c='C1')
        arrow((x[i0], y[j0 - 1] + hy * 0.5), (-hx, 0), c='C2')
        ax.text(x[i0] - hx * 0.8, y[j0 - 1] + hy * 0.65, r"$\Delta x$")
        ax.text(x[i0] - hx * 0.6, y[j0 - 1] - hy * 0.4, r"$c\Delta t$")

    ax.grid(lw=0.5)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(x[0], y[-1])
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$t$')
    ax.set_xticks(x, map(lambda q: '{:.2g}'.format(q), x))
    ax.set_yticks(y, map(lambda q: '{:.2g}'.format(q), y))
    ax.set_aspect('equal')
    savefig(fig, suff=suff)
    plt.close(fig)


run(None, suff='', noscat=True)
run(None, suff='_cfl0')
run(0.6, suff='_cfl1')
run(1.5, suff='_cfl2')
run(-0.5, suff='_cfl3')
run(0.6, suff='_cfl4', arr=True)
run(0.6, suff='_cfl5', both=True)
