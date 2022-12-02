#!/usr/bin/env python3

import numpy as np

A = np.array([
    [5., 1., 1.],
    [1., 6., 1.],
    [1., 1., 7.],
])
I = np.eye(A.shape[0])

# Reference solution.
d, vv = np.linalg.eig(A)
i = 0
lamb = d[i]
v = vv[:, i]

maxiter = 100
tol = 1e-14

# Initial guess for eigenvector.
x = np.array([1, 1, 1])

for it in range(maxiter):
    # Rayleigh quotient.
    sigma = (x.T @ A @ x) / (x.T @ x)

    # Inverse iteration.
    y = np.linalg.solve(A - sigma * I, x)
    x = y / np.linalg.norm(y)

    err = np.linalg.norm(A @ x - sigma * x)
    print("\nit={:}".format(it))
    print("|Ax - sigma x|   = {:.16e}".format(err))
    print("|sigma - lambda| = {:.16e}".format(abs(sigma - lamb)))
    if err < tol:
        break

print("\nlambda = {:.16e}".format(lamb))
print("sigma  = {:.16e}".format(sigma))
print("\nv  = {:}".format(v))
print("x  = {:}".format(x))
