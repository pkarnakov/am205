#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import get_path, savefig


def run(c, suff):
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.set_axis_off()
    nx = 7
    ny = 2

    x = np.linspace(0, 1, nx)
    qx = 4
    qxe = 2
    h = x[1] - x[0]
    s = 8

    gap = 0.5
    shx = -0.05 * h

    def arrow(xy, dxy, c='k', lw=0.002):
        xy = np.array(xy)
        dxy = np.array(dxy)
        ax.arrow(
            *xy,
            *dxy,
            color=c,
            lw=lw * 200,
            overhang=0.2,
            head_width=lw * 7,
            head_length=lw * 10,
            length_includes_head=True,
            zorder=8,
        )

    for i in range(qx):
        ax.scatter(x[i], h, clip_on=False, c='k', s=s, edgecolor='none')
        ax.scatter(x[i], 0, clip_on=False, c='k', s=s, edgecolor='none')
        ax.text(x[i] + shx,
                -h * 0.1,
                r"${:d}$".format(i),
                ha='right',
                va='top')
        t = r"$N_x\!+\!{:d}$".format(i) if i > 0 else "$N_x$"
        ax.text(x[i] + shx, h - h * 0.1, t, ha='right', va='top')
        if i > 0:
            ax.plot([x[i], x[i - 1]], [0, 0], c='k')
            ax.plot([x[i], x[i - 1]], [h, h], c='k')
        ax.plot([x[i], x[i]], [0, h], c='k')
        ax.plot([x[i], x[i]], [h, h * (1 + gap)], c='k', ls='--')
        if i == qx - 1:
            ax.plot([x[i], x[i] + h * gap], [h, h], c='k', ls='--')
            ax.plot([x[i], x[i] + h * gap], [0, 0], c='k', ls='--')

    for ii in range(qxe):
        i = nx - ii - 1
        ax.scatter(x[i], 0, clip_on=False, c='k', s=s, edgecolor='none')
        ax.scatter(x[i], h, clip_on=False, c='k', s=s, edgecolor='none')
        ax.text(x[i] + shx,
                -h * 0.1,
                r"$N_x\!-\!{:d}$".format(ii + 1),
                ha='right',
                va='top')
        ax.text(x[i] + shx,
                h - h * 0.1,
                r"$2N_x\!-\!{:d}$".format(ii + 1),
                ha='right',
                va='top')
        if ii > 0:
            ax.plot([x[i], x[i + 1]], [0, 0], c='k')
            ax.plot([x[i], x[i + 1]], [h, h], c='k')
        ax.plot([x[i], x[i]], [0, h], c='k')
        ax.plot([x[i], x[i]], [h, h * (gap + 1)], c='k', ls='--')
        if ii == qxe - 1:
            ax.plot([x[i], x[i] - h * gap], [h, h], c='k', ls='--')
            ax.plot([x[i], x[i] - h * gap], [0, 0], c='k', ls='--')

    dx = h * 0.1
    dy = h * 0.1
    arrow((h, -h * 0.6 + dy), (h * 4, 0))
    arrow((-h * 0.6 + dx, 0), (0, h * 1.5))
    ax.text(h * 3, -h * 0.75 + dy, "$i$", ha='right', va='top')
    ax.text(-h * 0.75 + dx, 0.8 * h, "$j$", ha='right', va='top')

    ax.set_xlim(-0.75 * h, 1 + 0.2 * h)
    ax.set_ylim(-0.75 * h, 1.8 * h)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_aspect('equal')
    savefig(fig, suff=suff)
    plt.close(fig)


run(None, suff='')
