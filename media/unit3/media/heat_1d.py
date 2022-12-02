#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import get_path, savefig


def heat_system(h, ff):
    N = len(ff)
    d = np.zeros(N)
    a = np.zeros(N)
    b = np.zeros(N)
    c = np.zeros(N)
    for i in range(1, N - 1):
        a[i] = -1 / h ** 2
        b[i] = 2 / h ** 2
        c[i] = -1 / h ** 2
        d[i] = ff[i]
    # Left: zero value.
    b[0] = 1
    # Right: zero derivative.
    a[-1] = -1
    b[-1] = 1
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


N = 64

x = np.linspace(-1, 1, N)
h = x[1] - x[0]

ff = 1 - x ** 2

L = heat_system(h, ff)
u = tdma(*L)

fig, ax = plt.subplots()
ax.set_ylim(0, 1.5)
ax.set_yticks(np.arange(0, 1.51, 0.5))
ax.plot(x, u, c='C0', label='u(x)')
ax.plot(x, ff, c='k', label='f(x)')
ax.set_xlabel('x')
ax.legend()
savefig(fig)
plt.close(fig)
