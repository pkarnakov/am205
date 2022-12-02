#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import get_path, savefig


def heat_system(h, dt, f, u):
    N = len(f)
    d = np.zeros(N)
    a = np.zeros(N)
    b = np.zeros(N)
    c = np.zeros(N)
    for i in range(1, N - 1):
        a[i] = -1 / h ** 2
        b[i] = 1 / dt + 2 / h ** 2
        c[i] = -1 / h ** 2
        d[i] = f[i] + u[i] / dt
    # Given derivatives.
    b[0] = 1
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
Nt = 80
tmax = 4

x = np.linspace(-1, 1, N)
h = x[1] - x[0]
dt = tmax / Nt
f = 1 - x ** 2
u = np.zeros_like(x)

fig, ax = plt.subplots()

for it in range(Nt + 1):
    L = heat_system(h, dt, f, u)
    u = tdma(*L)
    t = it * dt
    if (it % (Nt // tmax) == 0 and t >= 1) or (it == 5):
        ax.plot(x, u, label='u(x,{:.2g})'.format(t))

ax.set_ylim(0, 1.5)
ax.set_yticks(np.arange(0, 1.51, 0.5))
ax.plot(x, f, c='k', label='f(x)')
ax.set_xlabel('x')
ax.legend(bbox_to_anchor=(1.1,0.8))
savefig(fig)
plt.close(fig)
