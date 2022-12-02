#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path


# Evaluates the sum of exponentials.
def sum_exp(x, b):
    res = 0
    n = len(b) // 2
    for i in range(len(b)):
        res += b[i] * np.exp((i - n) * x)
    return res

# Returns a matrix `A` with `lenb` columns
# such that `Ab` equals `sum_exp(x, b)`.
def matrix_exp(x, lenb):
    n = lenb // 2
    A = np.array([np.exp((i - n) * x) for i in range(lenb)]).T
    return A


# Data points.
xp = np.linspace(-1, 1, 20)
yp = np.exp(-xp) * np.cos(4 * xp)

xnew = np.linspace(-1, 1, 1001)

dat = open(get_path('dat'), 'w')

for n in [1, 2, 3]:
    A = matrix_exp(xp, 2 * n + 1)

    b = np.linalg.lstsq(A, yp, rcond=None)[0]

    fig, ax = plt.subplots()

    r = np.linalg.norm(A @ b - yp)
    dat.write('n={:} |Ab-y|={:.2f}\n'.format(n, r))

    ax.scatter(xp, yp, clip_on=False, zorder=5, c='k')
    ax.plot(xnew, sum_exp(xnew, b))

    ax.set_xlim(-1, 1)
    ax.set_ylim(-3, 2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    suff = "_n{:}".format(n)
    savefig(fig, suff=suff)
    plt.close(fig)

dat.close()
