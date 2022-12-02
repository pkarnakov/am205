#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path

xlim = (-4, 2)
ylim = (-3, 3)
x1 = np.linspace(*xlim, 500)
y1 = np.linspace(*ylim, 500)

x, y = np.meshgrid(x1, y1)


def f(y):
    return y


def rk1(f, y, h):
    k1 = f(y)
    y += h * k1
    return y


# Midpoint
def rk2_midpoint(f, y, h):
    k1 = f(y)
    k2 = f(y + h * k1 / 2)
    y += h * k2
    return y

# Ralston's third-order
def rk3_ralston(f, y, h):
    k1 = f(y)
    k2 = f(y + h * k1 / 2)
    k3 = f(y + h * k2 * 3 / 4)
    y += h * (2 * k1 + 3 * k2 + 4 * k3) / 9
    return y

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
    k1 = f(y)
    k2 = f(y + h * k1 / 2)
    k3 = f(y + h * k2 / 2)
    k4 = f(y + h * k3)
    y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


def rk(p, f, y, h):
    return [rk1, rk2, rk3, rk4][p - 1](f, y, h)


fig, ax = plt.subplots(figsize=(2, 2))
z = x + y * 1j

for p, c, lbl in [
    (1, 'C0', r'p=1'),
    (2, 'C1', r'p=2'),
    (3, 'C2', r'p=3'),
    (4, 'C3', r'p=4'),
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
ax.set_xticks(range(xlim[0], xlim[1] + 1))
ax.set_yticks(range(ylim[0], ylim[1] + 1))
ax.axvline(x=0, lw=0.5, ls='-', c='k', zorder=-5)
ax.axhline(y=0, lw=0.5, ls='-', c='k', zorder=-5)
ax.legend(bbox_to_anchor=(1.4,1))
savefig(fig)
plt.close(fig)
