#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from util import savefig

# Define a vector.
x = np.array([1.2, 0.5, -0.1, 2.3, -1.05, -2.35])
n = len(x)

# Calculate the p-norm for a range of values of p.
pp = np.linspace(1, 20)
norm_p = [sum(abs(x)**p)**(1 / p) for p in pp]

# Calculate the infinity norm.
norm_inf = np.array([max(abs(x))] * len(pp))

# Calculate the upper bound.
upper = n ** (1 / pp) * norm_inf

# Plot.
fig, ax = plt.subplots()
ax.plot(pp, norm_p, c='C0', label=r'$\Vert x \Vert_p$')
ax.plot(pp, norm_inf, c='C1', label=r'$\Vert x \Vert_\infty$')
ax.plot(pp, upper, c='C1', ls='--', label=r'$n^{1/p}\;\Vert x \Vert_\infty$')
ax.set_xlabel('$p$')
ax.set_ylabel('norm value')
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
ax.legend()
savefig(fig)
plt.close(fig)
