#!/usr/bin/env python3

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy.interpolate
from util import get_path, savefig

xp = np.linspace(0, 2, 11)
xnew = np.linspace(0, 2, 500)
yp0 = xp * (xp - 1) * (xp - 1.5) + 3
np.random.seed(33)
yp = yp0 + 0.05 * np.random.normal(size=len(xp))

def plot(isel, dx, dy, frame=None, ext='svg', force=False, poly=False):
    suff = '_poly' if poly else '_spline'
    suff = suff if frame is None else '{}_{:04d}'.format(suff, frame)
    path = get_path(ext, suff)
    if os.path.isfile(path) and not force:
        print("skip existing '{}'".format(path))
        return

    fig, ax = plt.subplots()
    ax.scatter(xp, yp, clip_on=False, zorder=5, c='k')

    bc_type = ((1, 0), (1, 0))

    if poly:
        f = np.poly1d(np.polyfit(xp, yp, len(xp) - 1))
    else:
        f = scipy.interpolate.CubicSpline(xp, yp, bc_type=bc_type)
    ynew = f(xnew)
    ax.plot(xnew, ynew, clip_on=False)

    xpm = np.copy(xp)
    ypm = np.copy(yp)
    xpm[isel] += dx
    ypm[isel] += dy
    if poly:
        fm = np.poly1d(np.polyfit(xpm, ypm, len(xpm) - 1))
    else:
        fm = scipy.interpolate.CubicSpline(xpm, ypm, bc_type=bc_type)
    ymnew = fm(xnew)
    ax.plot(xnew, ymnew)
    ax.scatter([xpm[isel]], ypm[isel], c='k', marker='x', zorder=5, s=10)

    diff = (ymnew - ynew)
    yref = 3.75
    ix = np.argmin(abs(xnew - xp[isel]))
    diff = diff / (abs(diff).max() + 1e-8) + yref
    ax.plot(xnew, diff, clip_on=False)
    ax.axhline(y=yref, ls='--', c='k', zorder=-1)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_ylim(2.5, 5)

    savefig(fig, ext=ext, suff=suff, dpi=197)
    plt.close(fig)


isel = 3
plot(isel=isel, dx=0., dy=1.5, ext='svg', poly=False)
plot(isel=isel, dx=0., dy=1.5, ext='svg', poly=True)

angles = np.linspace(-0.5 * np.pi, 1.5 * np.pi, 100, endpoint=False)
angles += (angles[1] - angles[0]) * 0.5
for frame, angle in enumerate(angles):
    dx = np.cos(angle) * (xp[1] - xp[0]) * 0.65
    q = 1.7
    dy = (np.exp(np.sin(angle) * q) - np.exp(-q)) * 0.3 + 0.1
    plot(isel=isel, dx=dx, dy=dy, frame=frame, ext='png', force=True, poly=False)
    plot(isel=isel, dx=dx, dy=dy, frame=frame, ext='png', force=True, poly=True)
