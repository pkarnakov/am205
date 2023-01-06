#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
from numpy.polynomial.chebyshev import chebroots

def fmain(x):
    return 0

def peak(x, x0, dy, eps=3e-2):
    return dy * np.maximum(0, 1 - abs(x - x0) / eps)

# Evaluates the Lagrange interpolant.
def lagrange(x, xp, yp):
    res = 0
    for i in range(len(xp)):
        prod = 1
        for j in range(len(xp)):
            if j != i:
                prod *= (x - xp[j]) / (xp[i] - xp[j])
        res += yp[i] * prod
    return res


n = 3  # Points.

cheb = chebroots([0] * n + [1])
f = lambda x: fmain(x) + peak(x, cheb[0], 1)

plt.figure(figsize=(2, 1.7))
for case in ['cheb', 'equi']:
    if case == 'cheb':
        xp = chebroots([0] * n + [1])
        c = 'C0'
        m = 's'
    elif case == 'equi':
        xp = np.linspace(-1, 1, n)
        c = 'C1'
        m = 'o'
    else:
        assert False
    yp = f(xp)

    xx = np.linspace(-1, 1, 1001)
    yy = f(xx)
    yyi = lagrange(xx, xp, yp)

    #plt.plot(xx, abs(yyi - yy), label=case, c=c)
    ms = 2
    plt.plot(xx,
             yyi,
             label=case,
             c=c,
             lw=1,
             markersize=ms,
             marker=m,
             markevery=(len(xx), 1))
    plt.plot(xp, yp, c=c, lw=0, zorder=6, markersize=ms, marker=m)
plt.plot(xx, yy, label="f(x)", zorder=10, c='k', lw=0.5)
plt.legend()
plt.xlim(-1.2, 1.2)
plt.ylim(-0.5, 1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("q7_cheb_equi.pdf", bbox_inches='tight')
