#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.chebyshev import Chebyshev, chebinterpolate

def get_path(ext, suff=''):
    return os.path.splitext(os.path.basename(
        sys.argv[0]))[0] + suff + '.' + ext


def savefig(fig, suff=''):
    path = get_path('svg', suff)
    print(path)
    fig.savefig(path, metadata={'Date': None})

def f_runge(x):
    return 1 / (1 + 25 * x ** 2)

def f_abs(x):
    return abs(x)

x = np.linspace(-1, 1, 1000)

fig, ax = plt.subplots()
degs = range(61)
err_runge = []
err_abs = []
for f, err in [(f_runge, err_runge), (f_abs, err_abs)]:
    for deg in degs:
        p = chebinterpolate(f, deg)
        fp = Chebyshev(p)
        err.append(np.max(abs(fp(x) - f(x))))

# Runge function and its derivatives.
ax.plot(degs, np.log10(err_runge), c='C0', label=r"Runge")
ax.plot(degs, np.log10(err_abs), c='C1', label=r"$|x|$")
ax.set_xlabel('degree')
ax.set_ylabel(r'$\log_{10}(E_\mathrm{inf})$')
ax.legend()
savefig(fig)
plt.close(fig)
