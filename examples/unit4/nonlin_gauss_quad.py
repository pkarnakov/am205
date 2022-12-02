#!/usr/bin/env python3
import numpy as np
import scipy.optimize

count_f = 0
count_fprime = 0


# Vector function, conditions of 2-point Gauss quadrature.
def f(x):
    global count_f
    count_f += 1

    x1, x2, w1, w2 = x
    x1s = x1 * x1
    x2s = x2 * x2
    f = np.array([
        w1 + w2 - 2,
        w1 * x1 + w2 * x2,
        w1 * x1s + w2 * x2s - 2. / 3,
        w1 * x1s * x1 + w2 * x2s * x2,
    ])
    return f


# Exact Jacobian, 4x4 matrix.
def fprime(x):
    global count_fprime
    count_fprime += 1

    x1, x2, w1, w2 = x
    x1s = x1 * x1
    x2s = x2 * x2
    return np.array([
        [0, 0, 1, 1],
        [w1, w2, x1, x2],
        [2 * w1 * x1, 2 * w2 * x2, x1s, x2s],
        [3 * w1 * x1s, 3 * w2 * x2s, x1s * x1, x2s * x2],
    ])


# Custom implementation of Newton's method.
def newton(x0, tol=1e-13, maxiter=100):
    xk = x0
    fk = f(xk)
    err = np.linalg.norm(fk)
    for i in range(maxiter):
        if err < tol:
            break
        xk -= np.linalg.solve(fprime(xk), fk)
        fk = f(xk)
        err = np.linalg.norm(fk)
    return xk


# Scipy implementation of Powell's hybrid method, with exact Jacobian.
def fsolve_jac(x0, tol=1e-13, maxiter=100):
    xk = scipy.optimize.fsolve(f, x0, fprime=fprime, xtol=tol, maxfev=maxiter)
    return xk


# Scipy implementation of Powell's hybrid method, with approximate Jacobian.
def fsolve(x0, tol=1e-13, maxiter=100):
    xk = scipy.optimize.fsolve(f, x0, xtol=tol, maxfev=maxiter)
    return xk


def run(solver, name):
    global count_f
    global count_fprime
    count_f = 0
    count_fprime = 0

    def print_red(msg):
        # Change output color using the ANSI escape sequences.
        # https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
        print("\033[31;1m" + str(msg) + "\033[0m")

    print_red("\n\nMethod: {}".format(name))

    # Initial guess:  x1, x2 (points); w1, w2 (weights)
    x0 = np.array([-1, 1, 1, 1]).astype(float)

    # Exact solution, 2-point Gauss quadrature.
    x_exact = np.array([-1 / 3**0.5, 1 / 3**0.5, 1, 1])

    x = solver(x0)

    print("""
Solution:
x1, x2 ={:20.16f} {:20.16f}
w1, w2 ={:20.16f} {:20.16f}""".format(*x))

    print("""
Error:
x1, x2 ={:20.5g} {:20.5g}
w1, w2 ={:20.5g} {:20.5g}""".format(*(x - x_exact)))

    print("\n{:} calls of f(), {:} calls of fprime()".format(
        count_f, count_fprime))


run(newton, "custom Newton")
run(fsolve_jac, "fsolve() with exact Jacobian")
run(fsolve, "fsolve() with approximate Jacobian")
