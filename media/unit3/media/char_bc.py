#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.integrate
from util import get_path, savefig

plt.rcParams.update({
    "axes.spines.left": True,
    "axes.spines.right": True,
})


def run(c, suff):
    fig, ax = plt.subplots(figsize=(1.7,1.7))
    xmax = 1
    xmin = 0
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, 1)
    for x0 in np.linspace(-1, 2, 14):
        lw = 0.005
        dy = 0.98
        dx = dy * c
        if c > 0 and x0 + dx > xmax:
            dx = xmax - x0
            dy = dx / c
        if c < 0 and x0 + dx < xmin:
            dx = xmin - x0
            dy = dx / c
        ax.arrow(
            x0 - 0.01 * c,
            0,
            dx,
            dy,
            color='C1',
            overhang=0.2,
            head_width=lw * 7,
            head_length=lw * 10,
            length_includes_head=True,
        )

    ax.set_xlabel('initial condition')
    ax.set_ylabel('boundary condition')
    if c < 0:
        ax.yaxis.set_label_position("right")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    ax.text(0, -0.1, r"$x=a$", ha='center')
    ax.text(1, -0.1, r"$x=b$", ha='center')
    savefig(fig, suff=suff)
    plt.close(fig)


run(1, suff='_pos')
run(-1, suff='_neg')
