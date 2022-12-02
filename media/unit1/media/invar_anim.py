#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.interpolate
from util import get_path, savefig


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
xp0 = np.linspace(-1, 1, 31)
xnew0 = np.linspace(-1, 1, 1001)


def plot(dx,
         sx,
         frame=None,
         ext='png',
         force=False,
         func='poly',
         suff='',
         xlim=(-1, 1)):
    suff = '_' + suff + '_' + func
    suff = suff if frame is None else '{}_{:04d}'.format(suff, frame)
    path = get_path(ext, suff)
    if os.path.isfile(path) and not force:
        print("skip existing '{}'".format(path))
        return

    xp = xp0
    yp = (np.sin(xp * 3.1 + 2.7) * 0.9 + 1) * 0.5
    xp = xp0 * sx + dx
    xnew = xnew0 * sx + dx

    nterms = 4

    if func == 'poly':
        A = np.vander(xp, nterms)
        b = np.linalg.lstsq(A, yp, rcond=None)[0]
        ynew = np.poly1d(b)(xnew)
    elif func == 'exp':
        A = matrix_exp(xp, nterms)
        b = np.linalg.lstsq(A, yp, rcond=None)[0]
        ynew = sum_exp(xnew, b)
    else:
        assert False

    fig, ax = plt.subplots(figsize=(3.5, 2.2))

    r = np.linalg.norm(A @ b - yp)

    ax.scatter(xp, yp, clip_on=False, zorder=5, c='k')
    ax.plot(xnew, ynew)

    ax.set_xlim(xlim)
    ax.set_ylim(0, 1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xticks(np.arange(min(xlim), max(xlim) + 0.1))

    savefig(fig, ext=ext, suff=suff, dpi=197)
    plt.close(fig)


times = np.linspace(0, 2, 100, endpoint=False)
times += (times[1] - times[0]) * 0.5
for suff in ['trans', 'scal']:
    for func in ['poly', 'exp']:
        for frame, t in enumerate(times):
            if suff == 'trans':
                dx = 1 - np.abs(1 - t)
                sx = 1
                xlim = (-1, 2)
            elif suff == 'scal':
                dx = 0
                sx = 1 + np.abs(1 - t) * 0.9
                xlim = (-2, 2)
            else:
                assert False
            plot(dx=dx, sx=sx, frame=frame, suff=suff, xlim=xlim, func=func)
