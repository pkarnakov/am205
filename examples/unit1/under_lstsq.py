#!/usr/bin/env python3

from math import *
import numpy as np
import matplotlib.pyplot as plt


# Vandermonde interpolation function
def vand_f(x, b):
    res = b[0]
    for i in range(len(b) - 1):
        res *= x
        res += b[i + 1]
    return res


n = 12

# Create data and a truncated Vandermonde matrix.
x = np.linspace(0.2, 1, 5)
A = np.vander(x, n)
y = np.cos(4 * x)

# Solve using the least-squares function.
b1 = np.linalg.lstsq(A, y, rcond=None)[0]
print("Residual(lstsq): {:.4g}".format(np.linalg.norm(A @ b1 - y)))

# Solve the regularized normal equations.
mu = 0.1
S = mu * np.identity(n)
AT = A.T
ATA = np.dot(AT, A)
STS = S.T @ S
M = ATA + STS
print("Condition number: ", np.linalg.cond(M))
b2 = np.linalg.solve(M, np.dot(AT, y))
print("Residual(normal): {:.4g}".format(np.linalg.norm(A @ b2 - y)))

# Plot results
xnew = np.linspace(0, 1, 200)
ynew_lstsq = vand_f(xnew, b1)
ynew_normal = vand_f(xnew, b2)

plt.figure(figsize=(4, 3))
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x, y, marker='.', label='data', c='k')
plt.plot(xnew, ynew_lstsq, label='lstsq')
plt.plot(xnew, ynew_normal, ls='--', label='normal+reg')
plt.legend()
plt.tight_layout()
plt.savefig('under_lstsq.pdf')
