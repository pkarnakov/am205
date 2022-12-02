#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from numpy import tan, cos, log10


# Function.
def f(x):
    return np.exp(5 * x)


# Exact derivative.
def df_exact(x):
    return 5 * np.exp(5 * x)


# Approximation (a).
def fd_a(f, x, h):
    return (f(x + h) - f(x)) / (h)


# Target point.
x = 1
d_ex = df_exact(x)

logh = np.array([-(1 + i * 0.5) for i in range(31)])
h = [10**lh for lh in logh]

# Approximate derivatives.
d_a = [fd_a(f, x, hh) for hh in h]

# Relative error.
logerr_a = [log10(abs(d - d_ex) / d_ex) for d in d_a]

# Absolute error.
logerr_a_abs = [log10(abs(d - d_ex)) for d in d_a]

# Plot.
fig, ax = plt.subplots()
ax.plot(logh, logerr_a, c='C0', label='a')
ax.set_xlabel('$log_{10}h$')
ax.set_ylabel('$log_{10}$(absolute error)')
ax.set_ylim(-8, 2)
fig.savefig('fd_abs.svg')

# Plot.
fig, ax = plt.subplots()
ax.plot(logh, logerr_a_abs, c='C0', label='a')
ax.set_xlabel('$log_{10}h$')
ax.set_ylabel('$log_{10}$(relative error)')
ax.set_ylim(-6, 4)
fig.savefig('fd_rel.svg')
