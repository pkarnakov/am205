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


def run(suff='', phi=0, anim=False):
    global ax
    global lwabs
    inf = 5
    height = 1.5
    ylim = 4
    lwabs = ylim * 0.009 / height
    path = get_path(suff=suff, ext='png' if anim else 'svg')
    if not os.path.isfile(path) or 1:
        fig, axes = plt.subplots(1, 2, figsize=(2.5 * height, height))
        for i, ax in enumerate(axes):
            ax.axvline(x=0, c='k', zorder=-5)
            ax.axhline(y=0, c='k', zorder=-5)
            ax.set_xlim(-ylim * 0.5, ylim * 0.5)
            ax.set_ylim(-ylim * 0.5, ylim * 0.5)
            ax.set_axis_off()
            xo = V(0, 0)
            e1 = V(1, 0)

            tt = np.linspace(0, 2 * np.pi, 300)

            A = np.array([
                [1, 1.5],
                [0, 1],
            ])
            (u, s, vt) = np.linalg.svd(A)
            v = vt.T
            v = rot_matr(phi) @ v
            v1 = v[:, 0]
            v2 = v[:, 1]

            if i == 0:
                xx = V(np.cos(tt), np.sin(tt))
                ax.plot(*xx, c='k')
                orthsign(xo, v1, w=lwabs * 6, zorder=-5)
                arrow(xo, v1, c='C0')
                arrow(xo, v2, c='C1')
                if not anim:
                    text(V(-1, -1.1), r'$S$')
                text(v1 * 1.26,
                     r'$v_1$',
                     ha='center',
                     va='center')
                text(v2 * 1.26,
                     r'$v_2$',
                     ha='center',
                     va='center')

            if i == 1:
                xx = V(np.cos(tt), np.sin(tt))
                xx = A @ xx
                ax.plot(*xx, c='k')
                av1 = A @ v1
                av2 = A @ v2
                Qh = rot_matr(0.001)
                nv1 = -orth(unit(A @ (Qh @ v1 - v1)))
                nv2 = -orth(unit(A @ (Qh @ v2 - v2)))
                arrow(xo, av1, c='C0')
                arrow(xo, av2, c='C1')
                if anim:
                    nv1[1] *= 0.7
                    nv2[1] *= 0.7
                    text(av1 + nv1 * 0.44,
                         r'$Av_1$',
                         ha='center',
                         va='center')
                    text(av2 + nv2 * 0.44,
                         r'$Av_2$',
                         ha='center',
                         va='center')
                else:
                    orthsign(xo, av1, w=lwabs * 6, zorder=-5)
                    text(V(0.5, -0.6), r'$AS$')
                    text(av1 + nv1 * 0.44 + (0.1,0 ),
                         r'$\sigma_1 u_1$',
                         ha='center',
                         va='center')
                    text(av2 + nv2 * 0.44 + (-0.1,-0.1),
                         r'$\sigma_2 u_2$',
                         ha='center',
                         va='center')

                # Phantom.
                if i == 1:
                    text(V(2.7, 0), '\ ')

            point(xo, c='k', s=3)

            ax.set_aspect('equal')
        fig.subplots_adjust(wspace=0.1)
        savefig(fig, ext=None, path=path)
        plt.close(fig)

run()
for i, phi in enumerate(np.linspace(-np.pi, np.pi, 30, endpoint=False)):
    run(anim=True, phi=phi, suff='_{:04d}'.format(i))
