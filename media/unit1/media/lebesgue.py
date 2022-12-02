#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from numpy.polynomial.chebyshev import chebroots
from util import savefig, get_path


# Computes the sum of absolute values of Lagrange polynomials
def lsum(x, xp):
    res = 0
    for k in range(xp.size):
        xc = xp[k]
        li = 1
        for l in range(xp.size):
            if l != k:
                li *= (x - xp[l]) / (xp[k] - xp[l])
        res += abs(li)
    return res


x = np.linspace(-1, 1, 2000)
xf = np.linspace(-1, 1, 10000)

dat = open(get_path('dat'), 'w')

for cheb in [False, True]:
    for deg in [10, 20, 30]:
        if cheb:
            xp = chebroots([0] * (deg + 1) + [1])
        else:
            xp = np.linspace(-1, 1, deg + 1)
        fig, ax = plt.subplots()
        y = lsum(x, xp)
        ax.plot(x, y, clip_on=False)
        ax.set_xlim(-1, 1)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        suff = "_cheb" if cheb else "_equi"
        suff += "_{:}".format(deg)
        dat.write('{} ymax={:.2f}\n'.format(suff, lsum(xf, xp).max()))
        savefig(fig, suff=suff)
        plt.close(fig)

dat.close()
