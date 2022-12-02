#!/usr/bin/env python3
import numpy as np


def f(x):
    return x * x - 4 * np.sin(x)


# Initial interval, assume f(a)*f(b)<0.
a = 1
b = 3
tol = 1e-3

# Bisection search.
while b - a > tol:
    print('a={:.5f} b={:.5f} f(a)={:.5f} f(b)={:.5f}'
          .format(a, b, f(a), f(b)))
    c = 0.5 * (b + a)
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root: {:.5f}".format(0.5 * (a + b)))
