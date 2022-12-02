#!/usr/bin/env python3

import numpy as np


def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    # Copy lower triangular part.
    for i in range(n):
        for j in range(0, i + 1):
            L[i, j] = A[i, j]
    # Compute L.
    for j in range(n):
        L[j, j] = L[j, j]**0.5
        for i in range(j + 1, n):
            L[i, j] /= L[j, j]
        for k in range(j + 1, n):
            for i in range(k, n):
                L[i, k] -= L[i, j] * L[k, j]
    return L


n = 5

# Define a tridiagonal matrix.
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 2
    if i > 0:
        A[i, i - 1] = 1
    if i + 1 < n:
        A[i, i + 1] = 1

L = cholesky(A)
Lnp = np.linalg.cholesky(A)

print("A =\n" + str(A))
print("\nL =\n" + np.array_str(L, precision=2))
print("\nLnp =\n" + np.array_str(Lnp, precision=2))
print("\nL L^T =\n" + str(L @ L.T))
