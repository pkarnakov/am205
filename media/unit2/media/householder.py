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
    ax.scatter(*x, **kwargs, zorder=zorder, s=s, edgecolor='none')


def line(xs, xe, **kwargs):
    ax.plot(*V(xs, xe).T, **kwargs)


def linerange(d, ks, ke, xc=V(0, 0), **kwargs):
    line(xc + ks * d, xc + ke * d, **kwargs)


def orth(x):
    return V(-x[1], x[0]) / norm(x)


def orthsign(xc, d, w, c='k'):
    d = d / norm(d)
    do = orth(d)
    pp = [xc + d * w, xc + d * w + do * w, xc + do * w]
    ax.plot(*V(pp).T, c=c)

def circle(xc, r, c='k'):
    ax.add_patch(Circle(xc, r, edgecolor=c, facecolor='none', linewidth=LW))

def text(x, s, **kwargs):
    ax.text(*x, s, **kwargs)

def arrow(xs, xe, c='k', **kwargs):
    ax.arrow(*xs,
             *(xe - xs),
             width=lwabs,
             head_width=lwabs*7,
             head_length=lwabs*10,
             lw=0,
             facecolor=c,
             overhang=0.2,
             length_includes_head=True,
             **kwargs)


for case in ['1', 'angles', '2']:
    path = get_path(suff='_' + case, ext='svg')
    if not os.path.isfile(path) or 1:
        inf = 5
        height = 1.5
        ylim = 2.2
        fig, ax = plt.subplots(figsize=(height, height))
        ax.axvline(x=0, c='k', zorder=-5)
        ax.axhline(y=0, c='k', zorder=-5)
        lwabs = ylim * 0.009 / height
        ax.set_xlim(-ylim * 0.5, ylim * 0.5)
        ax.set_ylim(-ylim * 0.5, ylim * 0.5)
        ax.set_axis_off()
        xo = V(0, 0)
        e1 = V(1, 0)

        x = V(0.4, 0.8) # Source point.
        point(x)
        text(x + (-0.02, 0.08), r'$x$')

        Fx = norm(x) * e1
        v = Fx - x
        H = orth(v)

        point(Fx)
        text(Fx + (0.02, -0.2), r'$\|x\| e_1$')

        arrow(x, Fx, zorder=0.4)
        text(Fx + (0.01, 0.2), r'$v$')

        xc = x + v * 0.5
        orthsign(xc, H, w=lwabs * 6)

        linerange(H, -inf, inf, c='k', ls='--')
        text(-H * 0.6 + (-0.05, -0.2), r'$H$')

        if case == '2':
            Fxm = -norm(x) * e1
            vm = Fxm - x
            Hm = orth(vm)

            point(Fxm)
            text(Fxm + (-0.5, -0.2), r'$-\|x\| e_1$')

            arrow(x, Fxm, zorder=0.4)
            text(Fxm + (-0.02, 0.15), r'$v^-$')

            xcm = x + vm * 0.5
            orthsign(xcm, Hm, w=lwabs * 6)

            linerange(Hm, -inf, inf, c='k', ls='--')
            text(Hm * 0.6 + (0.15, -0.2), r'$H^-$')


        if case == 'angles':
            circle(xo, norm(x))
            line(xo, x, c='k')
            text((0.15, 0.17), r'$\theta$')
            text((0.25, 0.02), r'$\theta$')

        ax.set_aspect('equal')
        savefig(fig, path=path)
        #savefig(fig, ext='pdf', path=path)
        plt.close(fig)
