#!/usr/bin/env python3

from math import *


# Composite trapezoid rule with `n` subintervals.
def trap(f, a, b, n):
    # Subinterval width.
    h = (b - a) / float(n)

    # Trapezoid formula.
    res = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        res += f(a + i * h)

    return res * h


# Composite Simpson rule with `n` subintervals.
def simp(f, a, b, n):
    # Subinterval width.
    h = (b - a) / float(n)

    # Simpson's formula.
    res = f(a) + f(b)
    for i in range(1, n):
        res += 4 * f(a + (i - 0.5) * h) + 2 * f(a + i * h)
    res += 4 * f(b - 0.5 * h)

    return res * h / 6.0


# Function to integrate.
def f(x):
    return sin(x)


a = 1
b = 5
# Exact.
ex = cos(a) - cos(b)

n = 1
while n <= 65536:
    print("n={:5d}   h={:9.7f}   trap={:+8.6e}   simp={:+8.6e}".format(
        n, (b - a) / float(n),
        trap(f, a, b, n) - ex,
        simp(f, a, b, n) - ex))
    n *= 2
