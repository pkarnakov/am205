#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.chebyshev import chebroots
from util import get_path, savefig

def runge(x):
    return 1 / (1 + 25 * x ** 2)

def runge_x(x):
    return -50 * x / (1 + 25 * x ** 2) ** 2

def runge_xx(x):
    return (3750 * x**2 - 50) / ((
        (15625 * x**2 + 1875) * x**2 + 75) * x**2 + 1)

x = np.linspace(-1.5, 1.5, 500)

ext = 'svg'

# Interpolation on equidistant points or Chebyshev points.
for cheb in [False, True]:
    for deg in [4, 5, 12, 13]:
        suff=("_cheb" if cheb else "") + "_deg{:}".format(deg)
        path = get_path(ext, suff)
        if os.path.isfile(path):
            print("skip existing '{}'".format(path))
            continue
        fig, ax = plt.subplots()
        ax.plot(x, runge(x), c='C0')

        if cheb:
            xp = chebroots([0] * (deg + 1) + [1])
        else:
            xp = np.linspace(-1, 1, deg + 1)

        ax.scatter(xp, runge(xp), c='C1', zorder=10)
        ax.set_title("degree {:}".format(deg), y=0.9)
        f = lagrange(xp, runge(xp))
        ax.plot(x, f(x), c='C1')

        ax.axvline(x=-1., c='k', ls='--', zorder=-1)
        ax.axvline(x=1., c='k', ls='--', zorder=-1)
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1., 1.5)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        savefig(fig, suff=suff, ext=ext)
        plt.close(fig)

# Runge function and its derivatives.
path = get_path(ext)
if os.path.isfile(path):
    print("skip existing '{}'".format(path))
else:
    fig, ax = plt.subplots()
    ax.plot(x, runge(x), c='C0', label=r"$f(x)$")
    ax.plot(x, runge_x(x), c='C1', label=r"$f'(x)$")
    ax.plot(x, runge_xx(x), c='C2', label=r"$f''(x)$")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-25, 15)
    ax.set_yticks([-25, -15, -5, 5, 15])
    ax.set_xlabel('x')
    ax.legend()
    savefig(fig, ext=ext)
    plt.close(fig)

# Spline interpolation.
suff = "_spline"
path = get_path(ext, suff=suff)
if os.path.isfile(path) and 0:
    print("skip existing '{}'".format(path))
else:
    from scipy.interpolate import CubicSpline
    fig, ax = plt.subplots()
    ax.plot(x, runge(x), c='C0')

    xp = np.linspace(-1, 1, 14)
    yp = runge(xp)

    ax.scatter(xp, yp, c='C1', zorder=10)
    f = CubicSpline(xp, yp)
    ax.plot(x, f(x), c='C1')

    ax.axvline(x=-1., c='k', ls='--', zorder=-1)
    ax.axvline(x=1., c='k', ls='--', zorder=-1)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1., 1.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    savefig(fig, suff=suff, ext=ext)
    plt.close(fig)
