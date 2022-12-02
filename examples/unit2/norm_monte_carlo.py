#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# Vector norm.
def vnorm(x):
    #return max(abs(x))  # Infinity-norm.
    return sum(x ** 2) ** 0.5 # 2-norm.

# Exact value of matrix norm induced by `vnorm()`.
def mnorm_exact(A):
    n = A.shape[0]
    #return max([sum(abs(A[i, :])) for i in range(n)])  # Infinity-norm.
    return np.linalg.norm(A, ord=2) # 2-norm.


n = 5

# Define a tridiagonal matrix.
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 3
    if i > 0:
        A[i, i - 1] = 1
    if i + 1 < n:
        A[i, i + 1] = 1


np.random.seed(2022)
nsamples = 100000
mm = [] # Current sample.
mmax = [-np.inf] # Current maximum.
mmin = [np.inf] # Current minimum.
ii = []  # Sample index.
for i in range(nsamples):
    x = np.random.rand(n) * 2 - 1 # Random values from [-1, 1].
    m = vnorm(A @ x) / vnorm(x)
    ii.append(i)
    mm.append(m)
    mmax.append(max(mmax[-1], m))
    mmin.append(min(mmin[-1], m))

mmax = mmax[1:]
mmin = mmin[1:]

print("Condition number (exact): ", np.linalg.cond(A))
print("Condition number (MC): ", mmax[-1] / mmin[-1])

# Plot.
plt.figure(figsize=(4, 4))
plt.scatter(ii, mm, s=2, alpha=0.5, edgecolor='none')
plt.plot(ii, mmax, c='g', label='max')
plt.plot(ii, mmin, c='b', label='min')
plt.axhline(y=mnorm_exact(A), c='g', ls='--', lw=2)
plt.axhline(y=1 / mnorm_exact(np.linalg.inv(A)), c='b', ls='--', lw=2)
plt.xlabel('number of samples')
plt.ylabel('matrix norm')
plt.legend(bbox_to_anchor=(0.74, 1.00))
plt.tight_layout()
plt.savefig("norm_monte_carlo.png", dpi=200)
