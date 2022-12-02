#!/usr/bin/env python3

h = 1.

while h > 1e-20:
    if 1 + h == 1:
        print("1+h=1:  {:.20g}".format(h))
    else:
        print("1+h!=1: {:.20g}".format(h))
    h *= 0.1
