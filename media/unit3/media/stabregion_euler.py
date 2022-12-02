#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path

xlim = (-3, 3)
ylim = (-3, 3)
x1 = np.linspace(*xlim, 500)
y1 = np.linspace(*ylim, 500)

x, y = np.meshgrid(x1, y1)

# Equation dy/dt = y.


def euler_forw(y, h):
    y += h * y
    return y


def euler_back(y, h):
    y = y / (1 - h)
    return y


z = x + y * 1j

def f(p, c, suff, rel=False):
    fig, ax = plt.subplots(figsize=(2, 2))
    if p == 1:
        r = np.abs(1 / (1e-8 / z - 1))
    if p == 2:
        r = np.abs(euler_forw(1, z))
        r2 = np.abs(euler_forw(1, 0.5 * z))
    elif p == 3:
        r = np.abs(euler_back(1, z))
        r2 = np.abs(euler_back(1, 0.5 * z))
    ax.contour(x1, y1, r, levels=[1.], colors=c)
    ax.contourf(x1, y1, r, levels=[0., 1.], colors=c, alpha=0.1)
    if not rel and (p == 2 or p == 3):
        ax.contour(x1, y1, r2, levels=[1.], colors=c)
        ax.contourf(x1, y1, r2, levels=[0., 1.], colors=c, alpha=0.1)

    if not rel:
        if p == 2:
            ax.text(-0.5, 0.3, r'$h=1$', ha='right')
            ax.text(-1.1, 1.3, r'$h=0.5$', ha='right')
        if p == 3:
            ax.text(1.5, 1, r'$h=1$', ha='left')
            ax.text(1.1, 2.1, r'$h=0.5$', ha='left')

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if rel:
        ax.set_xlabel(r'$\mathrm{Re}(h\lambda)$')
        ax.set_ylabel(r'$\mathrm{Im}(h\lambda)$')
    else:
        ax.set_xlabel(r'$\mathrm{Re}(\lambda)$')
        ax.set_ylabel(r'$\mathrm{Im}(\lambda)$')
    ax.set_aspect('equal')
    ax.set_xticks(range(xlim[0], xlim[1] + 1))
    ax.set_yticks(range(ylim[0], ylim[1] + 1))
    ax.axvline(x=0, lw=0.5, ls='-', c='k', zorder=-5)
    ax.axhline(y=0, lw=0.5, ls='-', c='k', zorder=-5)
    savefig(fig, suff='_' + suff)
    plt.close(fig)

f(1, 'C1', 'ode'),
f(2, 'C1', 'forw'),
f(3, 'C1', 'back'),
f(2, 'C1', 'forw_rel', rel=True),
f(3, 'C1', 'back_rel', rel=True),
