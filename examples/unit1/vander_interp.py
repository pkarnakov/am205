#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


# Evaluates polynomial with coefficients `b` using Horner's scheme.
def poly(x, b):
    res = b[0]
    for q in b[1:]:
        res *= x
        res += q
    return res


# Initialize points and function values.
n = 10  # Degree.
xp = np.linspace(0, 3, n + 1)
yp = np.exp(-xp)

# Solve Vandermonde problem.
v = np.vander(xp)
b = np.linalg.solve(v, yp)

# Optional random perturbation.
b += 1e-6 * np.random.rand(len(b))

xx = np.linspace(0, 3, 301)
yy = np.exp(-xx)
yyi = poly(xx, b)

plt.figure(figsize=(3, 3))
plt.plot(xx, yy, label="exp(-x)", lw=3)
plt.plot(xx, yyi, label="interpolant")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig("vander_interp.pdf", bbox_inches='tight')
