#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from util import savefig, get_path

LW = 0.5
plt.rcParams.update({
    "text.usetex": True,
    "lines.linewidth": LW,
})


def V(*v):
    return np.array(v)


def norm(x):
    return sum(x**2)**0.5


def point(x, s=5, zorder=5, **kwargs):
    ax.scatter(*x, **kwargs, zorder=zorder, s=s, clip_on=False, edgecolor='none')


def line(xs, xe, **kwargs):
    ax.plot(*V(xs, xe).T, **kwargs)


def linerange(d, ks, ke, xc=V(0, 0), **kwargs):
    line(xc + ks * d, xc + ke * d, **kwargs)


def orth(x):
    return V(-x[1], x[0]) / norm(x)


def text(x, s, **kwargs):
    ax.text(*x, s, **kwargs)


def orthsign(xc, d, w, c='k', **kwargs):
    d = d / norm(d)
    do = orth(d)
    pp = [xc + d * w, xc + d * w + do * w, xc + do * w]
    ax.plot(*V(pp).T, c=c, **kwargs)


def arrow(xs, xe, c='k', **kwargs):
    ax.arrow(*xs,
             *(xe - xs),
             width=lwabs,
             head_width=lwabs * 7,
             head_length=lwabs * 10,
             lw=0,
             facecolor=c,
             overhang=0.2,
             length_includes_head=True,
             **kwargs)

def unit(x):
    nx = np.linalg.norm(x)
    return x / (nx + 1e-10)

def rot_matr(phi):
    return np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])


def run(suff=''):
    global ax
    global lwabs

    np.random.seed(2022)

    inf = 5
    height = 1.5
    ylim = 4
    lwabs = ylim * 0.009 / height
    path = get_path(suff=suff, ext='svg')
    if not os.path.isfile(path) or 1:
        fig, ax = plt.subplots(figsize=(2.5 * height, height))
        ax.axvline(x=0, c='k', zorder=-5)
        ax.axhline(y=0, c='k', zorder=-5)
        ax.set_xlim(-ylim * 0.5, ylim * 0.5)
        ax.set_ylim(-ylim * 0.2, ylim * 0.5)
        ax.set_axis_off()
        xo = V(0, 0)
        e1 = V(1, 0)

        tt = np.linspace(0, 2 * np.pi, 300)

        B = np.array([
            [1, 1.5],
            [0, 1],
        ])

        x0 = V(0.25,0.5)

        N = 100
        xx = np.random.normal(size=(2, N)) * 0.4
        xx = B @ xx

        ax.scatter(*(xx+x0[:,None]), c='k', edgecolors='none', s=1)

        A = xx @ xx.T
        (u, s, vt) = np.linalg.svd(A)
        v = vt.T
        v1 = v[:, 0]
        v2 = v[:, 1]
        u1 = u[:, 0]
        u2 = u[:, 1]

        text((2, 0.2), r'$x$', ha='center', va='center')
        text((0.2, 1.9), r'$y$', ha='center', va='center')

        if suff == '_arrow':
            point(x0)
            vs1 = v1 * 1.2
            vs2 = v2 * 1.2
            arrow(x0, x0 + vs1, c='C0')
            arrow(x0, x0 + vs2, c='C1')
            text(x0 + vs1 * 1.1 + (0.2, 0.4),
                 r'$v_1$',
                 ha='center',
                 va='center')
            text(x0 + vs2 * 1.1 + (-0.1,-0.2),
                 r'$v_2$',
                 ha='center',
                 va='center')

        ax.set_aspect('equal')
        savefig(fig, ext=None, path=path)
        plt.close(fig)

run('')
run('_arrow')
