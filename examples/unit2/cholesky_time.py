#!/usr/bin/env python3

import numpy as np
import time
import sys


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

# Matrix size.
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 100
# Number of runs to average from. Decreases with `n` assuming complexity O(n^3)
count = max(1, 10000000 // n ** 3)

# Define a random symmetric positive definite matrix.
np.random.seed(2022)
A = np.random.uniform(-1, 1, size=(n, n))
A = A @ A.T

# `time.process_time()` returns time spent in current process in seconds.

print("n={:}, count={:}".format(n, count))

tstart = time.process_time()
for i in range(count):
    L = cholesky(A)
t_python = (time.process_time() - tstart) / count * 1e3
print("python: {:.3f} ms".format(t_python))

tstart = time.process_time()
for i in range(count):
    L = np.linalg.cholesky(A)
t_numpy = (time.process_time() - tstart) / count * 1e3
print("numpy: {:.3f} ms".format(t_numpy))

