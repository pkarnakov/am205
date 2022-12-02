#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

# Model parameters.
alpha1 = 1.2
beta1 = 0.4
alpha2 = 0.2
beta2 = 0.1


# Function that evaluates the RHS of the ODE. It has two components,
# representing the changes in prey and predator populations.
def f(t, y):
    return np.array([
        alpha1 * y[0] - beta1 * y[0] * y[1],
        -alpha2 * y[1] + beta2 * y[0] * y[1],
    ])


def step_from_tableau(alpha, beta, gamma, f, t, y, h):
    """
    Returns the solution after one step of a Runge-Kutta method
    specified by the Butcher tableau.

    alpha: list, length `n`
        First column, time value at each stage.
    beta: list of lists, length `n - 1`
        Triangular part.
    gamma: list, length `n`
        Solution coefficients.
    f: callable
       Function that takes (t, y) and returns the right-hand side.
    t: float
        Initial time.
    y: float or array
        Initial condition.
    h: float
        Step size.
    """
    n = len(alpha)  # Number of stages.
    k = []  # Intermediate evaluations.
    k.append(f(t + alpha[0], y))  # First stage.
    # Second and subsequent stages.
    for i in range(1, n):
        tt = t + alpha[i]
        yy = y
        for j in range(i):
            yy = yy + h * beta[i - 1][j] * k[j]
        k.append(f(tt, yy))
    yy = y
    for j in range(n):
        yy = yy + h * gamma[j] * k[j]
    return yy


def tableau_rk4():
    """
    Returns the Butcher tableau for the RK4 method.
    """
    alpha = [0, 0.5, 0.5, 1]
    beta = [
        [0.5],
        [0, 0.5],
        [0, 0, 1],
    ]
    gamma = [
        1. / 6,
        1. / 3,
        1. / 3,
        1. / 6,
    ]
    return alpha, beta, gamma


def tableau_rkf78():
    """
    Returns the Butcher tableau for the Fehlberg 7(8) method with n=13 stages.

    alpha: list, length `n`
        First column, time value at each stage.
    beta: list of rows, length `n - 1`
        Triangular part.
    gamma_low: list, length `n`
        Solution coefficients of order 7 method.
    gamma_high: list, length `n`
        Solution coefficients of order 8 method.
    """
    alpha = [
        0, 2. / 27, 1. / 9, 1. / 6, 5. / 12, 1. / 2, 5. / 6, 1. / 6, 2. / 3,
        1. / 3, 1., 0, 1
    ]
    beta = [
        [2. / 27],
        [1. / 36, 1. / 12],
        [1. / 24, 0, 1. / 8],
        [5. / 12, 0, -25. / 16, 25. / 16],
        [1. / 20, 0, 0, 1. / 4, 1. / 5],
        [-25. / 108, 0, 0, 125. / 108, -65. / 27, 125. / 54],
        [31. / 300, 0, 0, 0, 61. / 225, -2. / 9, 13. / 900],
        [2., 0, 0, -53. / 6, 704. / 45, -107. / 9, 67. / 90, 3],
        [
            -91. / 108, 0, 0, 23. / 108, -976. / 135, 311. / 54, -19. / 60,
            17. / 6, -1. / 12
        ],
        [
            2383. / 4100, 0, 0, -341. / 164, 4496. / 1025, -301. / 82,
            2133. / 4100, 45. / 82, 45. / 164, 18. / 41
        ],
        [
            3. / 205, 0, 0, 0, 0, -6. / 41, -3. / 205, -3. / 41, 3. / 41,
            6. / 41, 0
        ],
        [
            -1777. / 4100, 0, 0, -341. / 164, 4496. / 1025, -289. / 82,
            2193. / 4100, 51. / 82, 33. / 164, 12. / 41, 0, 1.
        ],
    ]
    gamma_low = [
        41. / 840, 0, 0, 0, 0, 34. / 105, 9. / 35, 9. / 35, 9. / 280, 9. / 280,
        41. / 840, 0, 0
    ]
    gamma_high = [
        0, 0, 0, 0, 0, 34. / 105, 9. / 35, 9. / 35, 9. / 280, 9. / 280, 0,
        41. / 840, 41. / 840
    ]
    return alpha, beta, gamma_low, gamma_high


def tableau_rkf7():
    alpha, beta, gamma, _ = tableau_rkf78()
    return alpha, beta, gamma


def tableau_rkf8():
    alpha, beta, _, gamma = tableau_rkf78()
    return alpha, beta, gamma


# Time points of interest.
t = np.linspace(0, 60, 60)

# Initial conditions, populations of prey and predators.
yinit = [10, 5]

fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(5, 8))

# Scipy.
yref = scipy.integrate.solve_ivp(f,
                                 t_span=(t[0], t[-1]),
                                 y0=yinit,
                                 t_eval=t,
                                 atol=1e-16,
                                 max_step=0.01).y[0]
ax0.plot(t, yref, label='scipy', c='k', lw=3)

sol = dict()
for tab, lbl in [
    (tableau_rk4, 'RK4'),
    (tableau_rkf7, 'RKF7'),
    (tableau_rkf8, 'RKF8'),
]:
    alpha, beta, gamma = tab()
    y = np.zeros((len(t), 2))
    y[0] = yinit
    for k in range(len(t) - 1):
        y[k + 1] = step_from_tableau(alpha, beta, gamma, f, t[k], y[k],
                                     t[k + 1] - t[k])
    l, = ax0.plot(t, y[:, 0], label=lbl)
    ax1.plot(t, abs(y[:, 0] - yref), c=l.get_color())
    sol[lbl] = y[:, 0]

ax1.plot(t, abs(sol['RKF7'] - sol['RKF8']), c='r', label='RKF7 - RKF8')

fig.legend(bbox_to_anchor=(1.2, 0.8))
ax0.set_xlabel('t')
ax0.set_ylabel('prey population')
ax1.set_ylabel('error')
ax1.set_yscale('log')
fig.savefig('fehlberg.pdf', bbox_inches='tight')
