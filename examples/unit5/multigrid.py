#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse
from functools import partial


# Returns the discrete Laplacian on `n` points, shape (n, n).
def get_A(n):
    res = np.zeros((n, n))
    res[0, 0] = 1
    res[-1, -1] = 1
    for i in range(1, n - 1):
        res[i, i - 1] = -1
        res[i, i] = 2
        res[i, i + 1] = -1
    res = scipy.sparse.csr_array(res)
    return res


# Returns interpolation matrix to `n` points, shape (n, n // 2 + 1).
def get_T(n):
    ncol = n // 2 + 1
    res = np.zeros((n, ncol))
    for i in range(n):
        if i % 2 == 0:
            res[i, i // 2] = 1
        else:
            res[i, i // 2] = 0.5
            res[i, i // 2 + 1] = 0.5
    res = scipy.sparse.csr_array(res)
    return res


# Returns restriction matrix from `n` points, shape (n // 2 + 1, n).
def get_R(n):
    nrow = n // 2 + 1
    res = np.zeros((nrow, n))
    res[0, 0] = 1
    res[-1, -1] = 1
    for i in range(1, nrow - 1):
        res[i, 2 * i - 1] = 0.25
        res[i, 2 * i] = 0.5
        res[i, 2 * i + 1] = 0.25
    res = scipy.sparse.csr_array(res)
    return res


# Full grid size.
n0 = 65
x = np.linspace(0, 1, n0)

# Exact solution on full grid.
u_exact = np.sin(4 * x * np.pi) + 0.5 * np.sin(16 * x * np.pi)

# Problem on full grid.
A0 = get_A(n0)
f0 = A0 @ u_exact

nlevels = 0
while 2**nlevels < n0:
    nlevels += 1

# Grid size for each level.
nn = [((n0 - 1) >> d) + 1 for d in range(nlevels)]
# Interpolation matrices.
TT = [get_T(n) for n in nn]
# Restriction matrices.
RR = [get_R(n) for n in nn]
# Discretization matrices.
AA = [None] * nlevels
AA[0] = A0
for level in range(1, nlevels):
    AA[level] = RR[level - 1] @ AA[level - 1] @ TT[level - 1]
# Diagonal parts of AA.
DD = [A.diagonal(0) for A in AA]
# Lower triangular parts of AA, including diagonals.
LL = [scipy.sparse.tril(A).tocsr() for A in AA]


def smoother_jacobi(level, u, f, omega=1.):
    A = AA[level]
    D = DD[level]
    u += ((f - (A @ u - D * u)) / D - u) * omega
    return u


def smoother_gauss_seidel(level, u, f):
    A = AA[level]
    L = LL[level]
    u = scipy.sparse.linalg.spsolve_triangular(L, f - (A @ u - L @ u))
    return u


def smoother_direct(level, u, f):
    u = scipy.sparse.linalg.spsolve(AA[level], f)
    return u


def multigrid(level, u, f, smoother, n_direct=2, max_level=None):
    '''
    smoother: `callable`
        Function `smoother(level, u, f)` returning an approximate solution of
           AA[level] u = f
        using initial guess `u`.
    '''
    if len(u) <= n_direct:
        return smoother_direct(level, u, f)
    r = RR[level] @ (f - AA[level] @ u)
    if max_level is None or level < max_level:
        u = u + TT[level] @ multigrid(
            level + 1, np.zeros_like(r), r, smoother, max_level=max_level)
    u = smoother(level, u, f)
    return u


u = np.zeros_like(x)
kk = []
rr = []
for k in range(50):
    kk.append(k)
    rr.append(np.linalg.norm(f0 - A0 @ u))
    u = multigrid(0, u, f0, max_level=4, smoother=smoother_gauss_seidel)

fig, ax = plt.subplots()
ax.plot(kk, rr)
ax.set_xlabel('k')
ax.set_ylabel('residual')
ax.set_yscale('log')
fig.savefig('multigrid_conv.pdf')

fig, ax = plt.subplots()
ax.plot(x, u, label='u')
ax.plot(x, u_exact, c='k', ls='--', label='exact')
ax.set_xlabel('x')
ax.set_ylabel('u')
ax.legend()
fig.savefig('multigrid_sol.pdf')
