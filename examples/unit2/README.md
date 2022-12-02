# AM205 Unit 2: Numerical Linear Algebra

## [`norm_inf.py`](norm_inf.py)

Shows that the p-norm converges to the infinity norm as `p` increases.

## [`norm_monte_carlo.py`](norm_monte_carlo.py)

Computes the matrix norm induced by a "black box" vector norm
using the Monte-Carlo method.

## [`cholesky.py`](cholesky.py)

Implements the Cholesky factorization algorithm, applies it to a tridiagonal
matrix and compares with the results of `numpy.linalg.cholesky`.

## [`cholesky_time.py`](cholesky_time.py)

Compares the execution time of Cholesky decomposition
implemented in Python using for-loops and `numpy.linalg.cholesky`.

## [`cholesky_time.cpp`](cholesky_time.cpp)

Measures the execution time of a C++ implementation of Cholesky decomposition.

## [`sparse.py`](sparse.py)

Demonstrates basic features of `scipy.sparse`.
Creates a sparse matrix in various formats (COO, CSR, CSC) and solves a linear 
system with that matrix.

## [`sparse_pattern.py`](sparse_pattern.py)

Visualizes the changes in the sparsity pattern during the LU and Cholesky
factorization algorithms.

## [`pca.py`](pca.py)

Performs the principal component analysis (PCA) on a two-dimensional data set.
