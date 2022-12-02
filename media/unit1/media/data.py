#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.interpolate
from util import get_path, savefig

def poly_latex(p):
    res = "y = "
    if not len(p):
        return res
    res += "{:.2f}".format(p[len(p) - 1])
    for i in range(1, len(p)):
        res += ' {:+.2f}'.format(p[len(p) - i - 1])\
                + ('x' if i else '') \
                + ('^{{{:}}}'.format(i) if i >= 2 else '')
    return res


x = np.linspace(0, 2, 11)
xnew = np.linspace(0, 2, 500)

y0 = x * (x - 1) * (x - 1.5) + 3

dat = get_path('dat')
if os.path.isfile(dat):
    y = np.loadtxt(dat)
else:
    np.random.seed(33)
    y = y0 + 0.05 * np.random.normal(size=len(x))
    np.savetxt(dat, y)

tex = open(get_path('tex'), 'w')

for suff in [
        '',
        '_piecewise_linear',
        '_poly',
        '_fit1',
        '_fit2',
        '_fit3',
        '_spline',
]:
    ext = 'svg'
    path = get_path(ext, suff)
    if os.path.isfile(path):
        print("skip existing '{}'".format(path))
        continue
    fig, ax = plt.subplots()
    ax.scatter(x, y, clip_on=False, zorder=5, c='k')
    ax.set_ylim(2.5, 5)
    if suff == '':
        pass
    if suff == '_piecewise_linear':
        ax.plot(x, y, clip_on=False)
    elif suff == '_poly':
        p = np.polyfit(x, y, len(x) - 1)
        f = np.poly1d(p)
        ax.plot(xnew, f(xnew), clip_on=False)
        tex.write("{}: {}\n".format(suff, poly_latex(p)))
    elif suff[:4] =='_fit':
        deg = int(suff[4:5])
        p = np.polyfit(x, y, deg)
        f = np.poly1d(p)
        ax.plot(xnew, f(xnew), clip_on=False)
        tex.write("{}: {}\n".format(suff, poly_latex(p)))
    elif suff == '_spline':
        bc_type = ((1, 0), (1, 0))
        f = scipy.interpolate.CubicSpline(x, y, bc_type=bc_type)
        ax.plot(xnew, f(xnew), clip_on=False)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    savefig(fig, suff, ext=ext)
    plt.close(fig)

tex.close()
