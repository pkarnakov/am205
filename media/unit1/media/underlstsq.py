#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from util import savefig, get_path


# Vandermonde interpolation function
def vand_f(x, b):
    res = b[0]
    for i in range(len(b) - 1):
        res *= x
        res += b[i + 1]
    return res


n = 12

# Create data and a truncated Vandermonde matrix.
xp = np.linspace(0.2, 1, 5)
A = np.vander(xp, n)
yp = np.cos(4 * xp)

xnew = np.linspace(-1, 1, 1001)

dat = open(get_path('dat'), 'w')

for case in [1, 2, 3, 4]:
    mu = {
        1: 0.001,
        2: 0.5,
        3: "case3",
        4: "case4",
    }[case]
    dat.write("\nn={:} mu={:}\n".format(n, mu))

    if case == 4:
        b = np.linalg.lstsq(A, yp, rcond=None)[0]
    else:
        AT = np.transpose(A)
        ATA = np.dot(AT, A)
        if case == 3:
            S = np.ones(n) * 10
            S[-3:] = 0.1
            S = np.diag(S)
        else:
            S = mu * np.identity(n)
        STS = S.T @ S
        dat.write("Condition number: {:.3g}\n".format(np.linalg.cond(ATA + STS)))
        b = np.linalg.solve(ATA + STS, np.dot(AT, yp))

    fig, ax = plt.subplots()

    r = np.linalg.norm(A @ b - yp)
    dat.write('case={:} |Ab-y|={:.3g}\n'.format(case, r))

    ax.scatter(xp, yp, clip_on=False, zorder=5, c='k')
    ax.plot(xnew, vand_f(xnew, b))

    ax.set_xlim(0, 1)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    suff = "_{:}".format(case)
    savefig(fig, suff=suff)
    plt.close(fig)

dat.close()
