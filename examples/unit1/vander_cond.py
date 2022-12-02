#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

nn = []
ncond = []

for n in range(2, 20):
    x = np.linspace(0, 1, n + 1)
    v = np.vander(x)
    nn.append(n)
    ncond.append(np.linalg.cond(v))

nn = np.array(nn)
log_ncond = np.log(ncond)

plt.figure(figsize=(3, 3))
plt.plot(nn, ncond, marker='o')

p = np.polyfit(nn, log_ncond, 1)
plt.plot(nn,
         np.exp(p[0] * nn + p[1]),
         label=r'${:.3g}\cdot{:.3g}^n$'.format(np.exp(p[1]), np.exp(p[0])))
plt.xlim(0, 20)
plt.yscale('log')
plt.xlabel('n')
plt.ylabel(r'$\mathrm{cond}(V_n)$')
plt.legend()
plt.tight_layout()
plt.savefig('vander_cond.pdf', bbox_inches='tight')
