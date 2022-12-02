#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.integrate
from util import get_path, savefig


xc = 1

def C1(x, t):
    return x - xc

def C2(x, t):
    return t - 1

t = np.linspace(0, 3, 500)

def traj_exact_1(x0):
    return xc + (x0 - xc) * np.exp(t)

def traj_exact_2(x0):
    return xc + 0.5 * t ** 2 - t

def traj(c, x0):
    x = scipy.integrate.odeint(c, x0, t)
    return x

fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
for x0 in np.linspace(0, 2, 21):
    ax.plot(traj(C1, x0), t, c='C0')
    #ax.plot(traj_exact_1(x0), t, c='C1')

ax.set_xlabel('x')
ax.set_ylabel('t')
savefig(fig)
plt.close(fig)

fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
for x0 in np.linspace(0, 2, 21):
    ax.plot(traj(C2, x0), t, c='C0')
    #ax.plot(traj_exact_2(x0), t, c='C1')

ax.set_xlabel('x')
ax.set_ylabel('t')
savefig(fig, suff='_2')
plt.close(fig)
