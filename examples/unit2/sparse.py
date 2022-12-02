#!/usr/bin/env python3

import scipy
from scipy.sparse import coo_array, csr_array, csc_array
import numpy as np

a = 1.
b = 2.
c = 3.

# Initialize CSR matrix.
data = np.array([a, b, b, b, b, c, c, c])
indices = np.array([0, 1, 2, 3, 4, 1, 2, 3])
indptr = np.array([0, 5, 6, 7, 8])
A_csr = csr_array((data, indices, indptr))
print("\nA_csr")
print("data=", A_csr.data)
print("indices=", A_csr.indices)
print("indptr=", A_csr.indptr)

# Convert to dense.
A_dense = A_csr.todense()
print("\nA_dense\n", A_dense)

# Convert to CSC.
A_csc = csc_array(A_dense)
print("\nA_csc")
print("data=", A_csc.data)
print("indices=", A_csc.indices)
print("indptr=", A_csc.indptr)

# Convert to COO.
A_coo = coo_array(A_dense)
print("\nA_coo")
print("data=", A_coo.data)
print("row=", A_coo.row)
print("col=", A_coo.col)

# Select a square submatrix.
B_csr = A_csr[:4, :4]
B_dense = A_dense[:4, :4]

# Right-hand side.
rhs = np.array([1., 2., 3., 4.])

# Solve linear system.
x_csr = scipy.sparse.linalg.spsolve(B_csr, rhs)
x_dense = scipy.linalg.solve(B_dense, rhs)
print("\nx_csr  =", x_csr)
print("x_dense=", x_dense)

# Residual.
x = x_dense
print("\nr_csr=", B_csr @ x - rhs)
print("r_dense=", B_dense @ x - rhs)
