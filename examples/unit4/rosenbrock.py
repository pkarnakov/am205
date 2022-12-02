#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

A = 100


# Rosenbrock function.
def f(xy):
    x, y = xy
    return A * (y - x**2)**2 + (1 - x)**2


# Gradient.
def f_grad(xy):
    x, y = xy
    return np.array([
        -4 * A * x * (y - x**2) - 2 * (1 - x),
        2 * A * (y - x**2),
    ])


# Hessian.
def f_hessian(xy):
    x, y = xy
    return np.array([[
        -4 * A * (y - x**2) + 8 * A * x**2 + 2,
        -4 * A * x,
    ], [
        -4 * A * x,
        2 * A,
    ]])


# Exact minimum.
exact_xy = (1, 1)

# Initial guess.
init_xy = np.array([-0.3, 1.5])


def newton(xy, maxiter=10):
    traj = [xy]
    for i in range(maxiter):
        dxy = np.linalg.solve(f_hessian(xy), -f_grad(xy))
        xy = xy + dxy
        traj.append(xy)
    return xy, traj


def bfgs(xy, maxiter=None):
    xy, traj = scipy.optimize.fmin_bfgs(
        f,
        x0=init_xy,
        maxiter=maxiter,
        fprime=f_grad,
        disp=False,  # No convergence message.
        retall=True,  # Return trajectory.
    )
    return xy, traj


xy, traj = newton(init_xy)
#xy, traj = bfgs(init_xy)

fig, ax = plt.subplots()

# Contours of logarithm of f(x,y).
xone = np.linspace(-2, 2, 256)
yone = np.linspace(-1, 3, 256)
xx, yy = np.meshgrid(xone, yone)
zz = np.log10(f((xx, yy)))
levels = np.linspace(-3, 3, 25)
contour = ax.contour(xx, yy, zz, levels=levels, cmap='jet', linewidths=0.75)
cbar = fig.colorbar(contour, label=r'$\log_{10} f$')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Trajectory.
ax.plot(*np.array(traj).T, c='k', marker='.')

# Initial guess.
ax.scatter(*init_xy, c='b', zorder=5, label='start')
# Exact minimum.
ax.scatter(*exact_xy, c='r', zorder=5, label='exact')
fig.legend(ncol=2)

fig.savefig('rosenbrock.pdf')
