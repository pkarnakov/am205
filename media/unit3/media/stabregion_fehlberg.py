#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path

xlim = (-8, 2)
ylim = (-5, 5)
x1 = np.linspace(*xlim, 1000)
y1 = np.linspace(*ylim, 1000)

x, y = np.meshgrid(x1, y1)


def f(y):
    return y


def rk1(f, y, h):
    k1 = f(y)
    y += h * k1
    return y


def step_from_tableau(alpha, beta, gamma, f, t, y, h):
    """
    Returns the solution after one step of a Runge-Kutta method
    specified by the Butcher tableau.

    alpha: list, length `n`
        First column, time value at each stage.
    beta: list of lists, length `n - 1`
        Triangular part.
    gamma: list, length `n`
        Solution coefficients.
    f: callable
       Function that takes (t, y) and returns the right-hand side.
    t: float
        Initial time.
    y: float or array
        Initial condition.
    h: float
        Step size.
    """
    n = len(alpha)  # Number of stages.
    k = []  # Intermediate evaluations.
    k.append(f(y))  # First stage.
    # Second and subsequent stages.
    for i in range(1, n):
        tt = t + alpha[i]
        yy = y
        for j in range(i):
            yy = yy + h * beta[i - 1][j] * k[j]
        k.append(f(yy))
    yy = y
    for j in range(n):
        yy = yy + h * gamma[j] * k[j]
    return yy


def tableau_rk4():
    """
    Returns the Butcher tableau for the RK4 method.
    """
    alpha = [0, 0.5, 0.5, 1]
    beta = [
        [0.5],
        [0, 0.5],
        [0, 0, 1],
    ]
    gamma = [
        1. / 6,
        1. / 3,
        1. / 3,
        1. / 6,
    ]
    return alpha, beta, gamma

def tableau_rkf78():
    """
    Returns the Butcher tableau for the Fehlberg 7(8) method with n=13 stages.

    alpha: list, length `n`
        First column, time value at each stage.
    beta: list of rows, length `n - 1`
        Triangular part.
    gamma_low: list, length `n`
        Solution coefficients of order 7 method.
    gamma_high: list, length `n`
        Solution coefficients of order 8 method.
    """
    alpha = [
        0, 2. / 27, 1. / 9, 1. / 6, 5. / 12, 1. / 2, 5. / 6, 1. / 6, 2. / 3,
        1. / 3, 1., 0, 1
    ]
    beta = [
        [2. / 27],
        [1. / 36, 1. / 12],
        [1. / 24, 0, 1. / 8],
        [5. / 12, 0, -25. / 16, 25. / 16],
        [1. / 20, 0, 0, 1. / 4, 1. / 5],
        [-25. / 108, 0, 0, 125. / 108, -65. / 27, 125. / 54],
        [31. / 300, 0, 0, 0, 61. / 225, -2. / 9, 13. / 900],
        [2., 0, 0, -53. / 6, 704. / 45, -107. / 9, 67. / 90, 3],
        [
            -91. / 108, 0, 0, 23. / 108, -976. / 135, 311. / 54, -19. / 60,
            17. / 6, -1. / 12
        ],
        [
            2383. / 4100, 0, 0, -341. / 164, 4496. / 1025, -301. / 82,
            2133. / 4100, 45. / 82, 45. / 164, 18. / 41
        ],
        [
            3. / 205, 0, 0, 0, 0, -6. / 41, -3. / 205, -3. / 41, 3. / 41,
            6. / 41, 0
        ],
        [
            -1777. / 4100, 0, 0, -341. / 164, 4496. / 1025, -289. / 82,
            2193. / 4100, 51. / 82, 33. / 164, 12. / 41, 0, 1.
        ],
    ]
    gamma_low = [
        41. / 840, 0, 0, 0, 0, 34. / 105, 9. / 35, 9. / 35, 9. / 280, 9. / 280,
        41. / 840, 0, 0
    ]
    gamma_high = [
        0, 0, 0, 0, 0, 34. / 105, 9. / 35, 9. / 35, 9. / 280, 9. / 280, 0,
        41. / 840, 41. / 840
    ]
    return alpha, beta, gamma_low, gamma_high


def tableau_rkf7():
    alpha, beta, gamma, _ = tableau_rkf78()
    return alpha, beta, gamma


def tableau_rkf8():
    alpha, beta, _, gamma = tableau_rkf78()
    return alpha, beta, gamma

# Heun's second-order
def rk2(f, y, h):
    k1 = f(y)
    k2 = f(y + h * k1)
    y += h * (k1 + k2) / 2
    return y

# Heun's third-order
def rk3(f, y, h):
    k1 = f(y)
    k2 = f(y + h * k1 / 3)
    k3 = f(y + h * k2 * 2 / 3)
    y += h * (k1 + 3 * k3) / 4
    return y


def rk4(f, y, h):
    alpha, beta, gamma = tableau_rk4()
    y = step_from_tableau(alpha, beta, gamma, f, 0, y, h)
    return y

def rkf7(f, y, h):
    alpha, beta, gamma, _ = tableau_rkf78()
    y = step_from_tableau(alpha, beta, gamma, f, 0, y, h)
    return y

def rkf8(f, y, h):
    alpha, beta, gamma, _ = tableau_rkf78()
    y = step_from_tableau(alpha, beta, gamma, f, 0, y, h)
    return y

def rk(p, f, y, h):
    if p == 'RKF7':
        return rkf7(f, y, h)
    elif p == 'RKF8':
        return rkf8(f, y, h)
    return [rk1, rk2, rk3, rk4][p - 1](f, y, h)


fig, ax = plt.subplots(figsize=(2, 2))
z = x + y * 1j

for p, c, lbl in [
    (1, 'C0', r'p=1'),
    (2, 'C1', r'p=2'),
    (3, 'C2', r'p=3'),
    (4, 'C3', r'p=4'),
    ('RKF7', 'C5', r'RKF7'),
]:
    r = np.abs(rk(p, f, 1, z))
    ax.plot([], [], c=c, label=lbl)
    ax.contour(x1, y1, r, levels=[1.], colors=c)
    ax.contourf(x1, y1, r, levels=[0., 1.], colors='k', alpha=0.1)

ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
ax.set_xlabel(r'$\mathrm{Re}(h\lambda)$')
ax.set_ylabel(r'$\mathrm{Im}(h\lambda)$')
ax.set_aspect('equal')
ax.set_xticks(range(xlim[0], xlim[1] + 1, 2))
ax.set_yticks(range(ylim[0], ylim[1] + 1, 2))
ax.axvline(x=0, lw=0.5, ls='-', c='k', zorder=-5)
ax.axhline(y=0, lw=0.5, ls='-', c='k', zorder=-5)
ax.legend(bbox_to_anchor=(1.4,1))
savefig(fig)
plt.close(fig)
