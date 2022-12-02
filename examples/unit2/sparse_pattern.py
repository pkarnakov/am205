#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# LU factorization without pivoting.
def lu(A):
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    plot(U, A, 'U', 'U=A')
    plot(L, np.eye(n), 'L', 'L=I')
    for j in range(n):
        for i in range(j + 1, n):
            L[i, j] = U[i, j] / U[j, j]
            for k in range(j, n):
                U[i, k] -= L[i, j] * U[j, k]
        input("j={:}".format(j))
        plot(U, A, 'U', 'U, j={:}'.format(j))
        plot(L, np.eye(n), 'L', 'L, j={:}'.format(j))
    return L, U


# Cholesky factorization.
def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    plot(L, A, 'L', 'L=0')
    for i in range(n):
        for j in range(0, i + 1):
            L[i, j] = A[i, j]
    for j in range(n):
        L[j, j] = L[j, j]**0.5
        for i in range(j + 1, n):
            L[i, j] /= L[j, j]
        for k in range(j + 1, n):
            for i in range(k, n):
                L[i, k] -= L[i, j] * L[k, j]
        input("j={:}".format(j))
        plot(L, A, 'L', 'L, j={:}'.format(j))
    return L


# Tridiagonal matrix.
def tridiag(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = 3
        if i > 0:
            A[i, i - 1] = 1
        if i + 1 < n:
            A[i, i + 1] = 1
    return A


def vander(n):
    return np.vander(np.linspace(1.1, 1.9, n))


# Tridiagonal matrix with periodic conditions.
def tridiag_periodic(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = 3
        if i > 0:
            A[i, i - 1] = 1
        if i + 1 < n:
            A[i, i + 1] = 1
    A[0, -1] = 1
    A[-1, 0] = 1
    return A


def random_matr(n):
    np.random.seed(2022)
    A = np.random.random((n, n))
    A[abs(A) < 0.9] = 0
    for i in range(n):
        A[i, i] = 1
    return A


def plot(A, A_init, suff='A', label=None):
    if label is None: label = suff
    colors = ['w', 'g', 'r']
    cmap = ListedColormap(colors)
    image = np.where(np.isclose(A, 0), 0, np.where(A_init != 0, 1, 2))
    fig, ax = plt.subplots(figsize=(13, 13))

    plt.pcolormesh(np.flipud(image),
                   vmin=0,
                   vmax=len(colors) - 1,
                   edgecolors='k',
                   cmap=cmap)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(label, fontsize=75, pad=20)
    ax.set_aspect('equal')
    fig.savefig('sparse_pattern_{}.png'.format(suff), bbox_inches='tight')
    plt.close(fig)


n = 30

#A = vander(n)
#A = tridiag(n)
#A = tridiag_periodic(n)
A = random_matr(n)
#A = A @ A.T

print(np.array_str(A, precision=2))
lu(A)
#cholesky(A)
