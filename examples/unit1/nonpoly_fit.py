#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt


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

n = 2
A = matrix_exp(xp, 2 * n + 1)

b = np.linalg.lstsq(A, yp, rcond=None)[0]

plt.figure(figsize=(3, 3))

r = np.linalg.norm(A @ b - yp)
print('|Ab-y|={:.3f}\n'.format(n, r))

plt.scatter(xp, yp, clip_on=False, zorder=5, c='k')
plt.plot(xnew, sum_exp(xnew, b))

plt.xlim(-1, 1)
plt.ylim(-3, 2)
plt.xlabel('x')
plt.ylabel('y')
suff = "_n{:}".format(n)
plt.tight_layout()
plt.savefig("nonpoly_fit.pdf")
