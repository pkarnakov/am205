#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


# Calculate the sum of absolute values of Lagrange basis polynomials.
def lsum(x, xp):
    res = 0
    for k in range(xp.size):
        xc = xp[k]
        li = 1
        for l in range(xp.size):
            if l != k:
                li *= (x - xp[l]) / (xp[k] - xp[l])
        res += abs(li)
    return res


# Control points (either linearly spaced, or Chebyshev)
n = 16
#xp = np.linspace(-1, 1, n)
xp = np.array([np.cos((2 * j + 1) * np.pi / (2 * n)) for j in range(n)])

# Sample points
xx = np.linspace(-1, 1, 1001)
yy = lsum(xx, xp)
print(yy.max())

# Plot figure using Matplotlib
plt.figure(figsize=(4,3))
plt.plot(xx, yy)
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig('lebesgue_const.pdf', bbox_inches='tight')
