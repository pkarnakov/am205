# AM205 Unit 0: Introduction

## [`precision.py`](precision.py)

Tests the value of machine epsilon, by comparing how small a value
of h is needed before 1+h evaluates to the same as 1.

Output example:

```
1+h!=1: 1
1+h!=1: 0.10000000000000000555
1+h!=1: 0.010000000000000001943
1+h!=1: 0.0010000000000000002377
1+h!=1: 0.0001000000000000000319
1+h!=1: 1.0000000000000004206e-05
1+h!=1: 1.0000000000000003783e-06
1+h!=1: 1.0000000000000004841e-07
1+h!=1: 1.0000000000000005172e-08
1+h!=1: 1.0000000000000004759e-09
1+h!=1: 1.0000000000000005534e-10
1+h!=1: 1.0000000000000005857e-11
1+h!=1: 1.0000000000000005857e-12
1+h!=1: 1.0000000000000006615e-13
1+h!=1: 1.0000000000000007877e-14
1+h!=1: 1.0000000000000008666e-15
1+h=1:  1.0000000000000009652e-16
1+h=1:  1.000000000000000996e-17
1+h=1:  1.0000000000000010345e-18
1+h=1:  1.0000000000000010586e-19
1+h=1:  1.0000000000000011489e-20
```

## [`precision.cpp`](precision.cpp)

A version of **precision.py** written in C++. With the GNU C++
compiler, the program can be compiled with
```
g++ -o precision precision.cpp
```
and then run with
```
./precision
```
It finds the same value of h as the Python version, emphasizing that what is
being tested is due to the hardware implementation of floating point
arithmetic, as opposed to being due to the specific programming language.

## [`rounding_control.cpp`](rounding_control.cpp)

Tests various rounding modes available in the C standard library
(and eventually in hardware).

Output example:

```
TONEAREST
    acosf(-1) = 3.141592741013
    1/3       = 0.333333343267
    5/3       = 1.666666626930
DOWNWARD
    acosf(-1) = 3.141592502593
    1/3       = 0.333333313465
    5/3       = 1.666666626930
UPWARD
    acosf(-1) = 3.141592741013
    1/3       = 0.333333343268
    5/3       = 1.666666746140
```
