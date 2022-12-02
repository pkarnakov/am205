#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import get_path, savefig
from numpy.polynomial.legendre import legroots

for n in [5, 10, 15, 20]:
    fig, ax = plt.subplots(figsize=(2.8, 1))
    xp = legroots([0] * n + [1])
    ax.scatter(xp, xp*0, c='C0', zorder=10)
    ax.set_title(r"$n={:}$".format(n), pad=-20)

    ax.set_title("{:} points".format(n), y=0.9)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_xlabel('x')
    savefig(fig, suff="_{:}".format(n))
    plt.close(fig)
