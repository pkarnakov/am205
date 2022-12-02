#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate

def f_runge(x):
    return 1 / (1 + 25 * x**2)


def f_abs(x):
    return abs(x)


# Evaluates the Lagrange interpolation.
def lagrange(x, xp, yp):
    res = 0
    for i in range(len(xp)):
        prod = 1
        for j in range(len(xp)):
            if j != i:
                prod *= (x - xp[j]) / (xp[i] - xp[j])
        res += yp[i] * prod
    return res


n = 20  # Degree.
f = f_runge # Function to interpolate.

ii = np.linspace(0, n, n + 1)
xp = np.cos((2 * ii + 1) * np.pi / (2 * (n + 1))) # Chebyshev roots.
#xp = np.linspace(-1, 1, n + 1)
yp = f(xp)

xx = np.linspace(-1, 1, 1001)
yy = f(xx)
yyi = lagrange(xx, xp, yp)
#yyi = scipy.interpolate.lagrange(xp, yp)(xx) # Numerically unstable.

plt.figure(figsize=(4, 3))
plt.plot(xx, yy, label="f(x)", lw=3)
plt.plot(xx, yyi, label="interpolant")
plt.legend(bbox_to_anchor=(1.5,0.5))
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("cheb_interp.pdf", bbox_inches='tight')
