#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Define a vector.
x = np.array([1.2, 0.5, -0.1, 2.3, -1.05, -2.35])
n = len(x)

# Calculate the p-norm for a range of values of p.
pp = np.linspace(1, 20)
norm_p = [sum(abs(x)**p)**(1 / p) for p in pp]

# Calculate the infinity norm.
norm_inf = [max(abs(x)) for p in pp]
upper = [n**(1 / p) * max(abs(x)) for p in pp]

# Plot.
plt.figure(figsize=(4, 3))
plt.plot(pp, norm_p, c='r', label='p-norm')
plt.plot(pp, norm_inf, c='g', label='infinity norm')
plt.plot(pp, upper, c='g', ls='--', label='upper bound')
plt.xlabel('p')
plt.ylabel('norm value')
plt.xlim(0, 20)
plt.ylim(0, 10)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("norm_inf.pdf")
