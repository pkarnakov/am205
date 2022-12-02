#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


# Function.
def f(x):
    return np.cos(x) * x


# Exact first derivative.
def df_exact(x):
    return np.cos(x) - np.sin(x) * x


# Exact second derivative.
def d2f_exact(x):
    return -np.sin(x) - np.sin(x) - np.cos(x) * x


fig, axes = plt.subplots(4, 1, figsize=(4, 8))

# Grid.
n = 31
x = np.linspace(0, 4, n)

# Differentiation matrix.
h = x[1] - x[0]
D = np.diag(-np.ones(n) / h) + np.diag(np.ones(n - 1) / h, 1)

# Backward difference in the last row.
D[n - 1, n - 2] = -1 / h
D[n - 1, n - 1] = 1 / h

# Evaluate function and derivatives.
y = f(x)
dy = D @ y
dy_exact = df_exact(x)

# Plot sparsity pattern.
ax = axes[0]
ax.spy(D, marker='s', markersize=2)

# Plot function.
ax = axes[1]
ax.set_ylabel('f(x)')
ax.plot(x, y)

# Plot derivative.
ax = axes[2]
ax.plot(x, dy_exact, label='exact')
ax.plot(x, dy, label='approx')
ax.set_ylabel("derivative")
ax.legend()

# Plot error.
ax = axes[3]
ax.plot(x, dy - dy_exact)
ax.set_xlabel('x')
ax.set_ylabel('error')

fig.tight_layout()
fig.savefig('diff_matr.pdf')
