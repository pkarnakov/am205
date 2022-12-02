#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path
from scipy.optimize import root


def xcenter(i, n):
    return (i - 1 - (n - 2) * 0.5) / ((n - 1) * 0.5)


def basis(x, i, n):
    if i == 0:
        return np.ones_like(x)
    return np.abs(x - xcenter(i, n))


# Evaluates the model.
def model(x, b):
    res = 0
    for i in range(len(b)):
        res += b[i] * basis(x, i, len(b))
    return res


# Returns a model_matrix `A` with `lenb` columns
# such that `Ab` equals `model(x, b)`.
def model_matrix(x, lenb):
    A = np.array([basis(x, i, lenb) for i in range(lenb)]).T
    return A


# Nonlinear. Basis.
def basis_nonlin(x, i, n, lamb):
    if i == 0:
        return np.ones_like(x)
    if i == n - 1:
        return np.abs(x - lamb)
    return np.abs(x - (i - 1 - (n - 2) * 0.5) / ((n - 1) * 0.5))


# Nonlinear. Evaluates the model.
def model_nonlin(x, b, lamb):
    res = 0
    for i in range(len(b)):
        res += b[i] * basis_nonlin(x, i, len(b), lamb)
    return res


# Nonlinear. Objective function.
def phi(bext):
    global xp, yp
    y = model_nonlin(xp, b=bext[:-1], lamb=bext[-1])
    res = 0.5 * ((y - yp)**2).sum()
    return res


# Nonlinear. Gradient of objective function.
def grad_phi(bext):
    global xp, yp
    res = np.zeros_like(bext)
    b = bext[:-1]
    lamb = bext[-1]
    n = len(b)
    dy = model_nonlin(xp, b, lamb) - yp
    for i in range(n):
        res[i] = np.dot(dy, basis_nonlin(xp, i, n, lamb))
    res[-1] = np.dot(dy, b[-1] * np.sign(lamb - xp))
    return res


# Data points.
xp = np.linspace(-0.75, 1.25, 20)
yp = abs(xp - 0.25) ** 0.5

xnew = np.linspace(-0.75, 1.25, 1001)
xnewb = np.linspace(-2, 2, 1001)

dat = open(get_path('dat'), 'w')

n = 3

for suff in ['basis', 'fit', 'basis_nonlin', 'fit_nonlin']:
    fig, ax = plt.subplots()
    ax.scatter(xp, yp, clip_on=False, zorder=5, c='k')
    if suff == 'fit':
        A = model_matrix(xp, n)
        b = np.linalg.lstsq(A, yp, rcond=None)[0]
        ax.plot(xnew, model(xnew, b))
        dat.write('{} n={:} b=[{}]\n'.format(
            suff, n, ', '.join(['{:.2f}'.format(bb) for bb in b])))
    if suff == 'basis':
        for i in range(n):
            ax.plot(xnewb,
                    basis(xnewb, i, n),
                    zorder=-5,
                    c='C{:}'.format(i + 1))
    if suff == 'fit_nonlin' or suff == 'basis_nonlin':
        # Levenberg-Marquardt.
        bext_init = [1] * n + [0.5]
        sol = root(grad_phi, bext_init, jac=False, method='lm')
        bext = sol.x
        if suff == 'fit_nonlin':
            dat.write('{} n={:} bext=[{}]\n'.format(
                suff, n, ', '.join(['{:.2f}'.format(bb) for bb in bext])))
            ax.plot(xnew, model_nonlin(xnew, b=bext[:-1], lamb=bext[-1]))
        if suff == 'basis_nonlin':
            for i in range(n):
                ax.plot(xnewb,
                        basis_nonlin(xnewb, i, n, lamb=bext[-1]),
                        zorder=-5,
                        c='C{:}'.format(i + 1))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0, 1.2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    savefig(fig, suff='_' + suff)
    plt.close(fig)

dat.close()
