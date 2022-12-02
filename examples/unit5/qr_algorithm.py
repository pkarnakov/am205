#!/usr/bin/env python3

import numpy as np

A = np.matrix([
    [2.9766, 0.3945, 0.4198, 1.1159],
    [0.3945, 2.7328, -0.3097, 0.1129],
    [0.4198, -0.3097, 2.5675, 0.6079],
    [1.1159, 0.1129, 0.6079, 1.7231],
])
maxiter = 100

# Initialization.
A_k = A.copy()
Q_prod = np.eye(A.shape[0])

# QR algorithm.
for it in range(maxiter):
    Q_k, R_k = np.linalg.qr(A_k)
    A_k = R_k @ Q_k
    Q_prod = Q_prod @ Q_k
    if it % 10 == 0:
        print("it={:3d} error={:.5e}".format(
            it, np.linalg.norm(A_k - np.diag(np.diag(A_k)))))

print("Result:")
print(np.diag(A_k))
print(Q_prod)

print("\nReference:")
D, V = np.linalg.eig(A)
print(D)
print(V)
