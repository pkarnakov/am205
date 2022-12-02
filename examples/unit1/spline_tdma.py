#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.interpolate


def spline_tridiag_system(xp, yp):
    N = len(xp)
    d = np.zeros(N)
    a = np.zeros(N)
    b = np.zeros(N)
    c = np.zeros(N)
    for i in range(1, N - 1):
        a[i] = 1 / (xp[i] - xp[i - 1])
        b[i] = 2 / (xp[i] - xp[i - 1]) + 2 / (xp[i + 1] - xp[i])
        c[i] = 1 / (xp[i + 1] - xp[i])
        d[i] = (
            3 * (yp[i] - yp[i - 1]) / (xp[i] - xp[i - 1])**2 +  #
            3 * (yp[i + 1] - yp[i]) / (xp[i + 1] - xp[i])**2)
    # Given derivatives.
    b[0] = 1
    d[0] = 0
    b[-1] = 1
    d[-1] = 0
    return a, b, c, d


def tdma(a, b, c, d):
    '''
    Solves equation:
                    b[0] * u[0]  + c[0] * u[1]     = d[0]
    a[i] * u[i-1] + b[i] * u[i]  + c[i] * u[i + 1] = d[i]
    a[-1] * u[-2] + b[-1] * u[-1]                  = d[-1]
    '''
    N = len(b)
    b = b.copy()
    d = d.copy()
    u = np.zeros(N)
    for i in range(1, N):
        m = a[i] / b[i - 1]
        b[i] -= m * c[i - 1]
        d[i] -= m * d[i - 1]
    u[-1] = d[-1] / b[-1]
    for i in reversed(range(N - 1)):
        u[i] = (d[i] - c[i] * u[i + 1]) / b[i]
    return u

def eval_spline(x, xp, yp, kp):
    '''
    xp, yp, kp: `array`
        Interpolation points, values, and first derivative.
    '''
    i = np.searchsorted(xp, x)  # xp[i-1] < x <= xp[i]
    i = np.maximum(np.minimum(i, len(xp) - 1), 1)
    # Polynomial in range [xp[i-1], xp[i]]
    dx = xp[i] - xp[i - 1]
    t = (x - xp[i - 1]) / dx
    a = yp[i] - yp[i - 1] - dx * kp[i]
    b = yp[i - 1] - yp[i] + dx * kp[i - 1]
    y = t * yp[i] + (1 - t) * yp[i - 1] + t * (1 - t) * (a * t + b * (1 - t))
    return y


xp = np.linspace(0, 2, 11)
xnew = np.linspace(0, 2, 500)

# Generate data.
yp0 = xp * (xp - 1) * (xp - 1.5) + 3
np.random.seed(33)
yp = yp0 + 0.05 * np.random.normal(size=len(xp))

plt.figure(figsize=(3, 3))
# Plot data.
plt.scatter(xp, yp, zorder=5, c='k', marker='.')

# Custom implementation.
system = spline_tridiag_system(xp, yp)
kp = tdma(*system)
plt.plot(xnew, eval_spline(xnew, xp, yp, kp), c='r')

# Spline from scipy.interpolate.
if 1:
    f = scipy.interpolate.CubicSpline(xp, yp, bc_type='clamped')
    plt.plot(xnew, f(xnew), zorder=-5, lw=3, c='g')

plt.xlabel('x')
plt.ylabel('y')
plt.ylim(2.5, 5)

plt.tight_layout()
plt.savefig('spline_tdma.pdf')
