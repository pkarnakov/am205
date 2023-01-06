---
title-meta:
- 'AM205 Quiz 1. Data fitting'
author-meta:
- 'Petr Karnakov'
---

# AM205 Quiz 1. Data fitting

## Q1

What is the minimal degree of a polynomial passing through the following
points

x | -1 | 0 | 1 | 2
-|-|-|-|-
y | 1  | 0 | 1 | 4

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4 or higher

## Q2

How many polynomials of degree $n$ pass through points
$S=\{(x_1,y_1),\ldots,(x_n,y_n)\}$ with distinct $x_1,\ldots,x_n$?

- [ ] zero
- [ ] one
- [ ] infinitely many
- [ ] depends on $S$

## Q3

Suppose that $f(x)$ is an interpolating spline of degree 5,
i.e. $f(x)$ is a piecewise polynomial of degree 5 in each of $n$ segments
$[x_{i-1}, x_{i}]$ for $i=1,\ldots,n$
and $f(x)$ passes through points $(x_i,y_i)$ for $i=0,\ldots,n$.
In addition, $f(x)$ is required to have 4 continuous derivatives in $[x_0,x_n]$.
How many additional constraints need to be imposed on $f(x)$ to guarantee
its uniqueness?

## Q4

Without accounting for the rounding error, which of the following polynomials
interpolates discrete data more accurately?

- [ ] an interpolating polynomial constructed in the monomial basis?
- [ ] an interpolating polynomial constructed in the Lagrange polynomial basis?
- [ ] both have the same accuracy

## Q5

Suppose that $L_i(x),\; i=0,\ldots,n$
represent the Lagrange polynomial basis on points $\{x_i\}$.
What is the degree of $g(x) = x \big(\sum_{i=0}^n{L_i(x)}\big)$?

## Q6

Which of the following are examples of nonlinear least-squares fitting
problems?

- [ ] fitting a straight line to discrete data
- [ ] fitting a quadratic polynomial *to* discrete data

## Q7

Interpolating polynomials are often used for function approximation.
Two common choices for the set of interpolation points are
the equidistant points and Chebyshev points.
Which of the two will produce a lower approximation error?

- [ ] equidistant points
- [ ] Chebyshev points
- [ ] depends on the function


## Q8

Linear least-squares fitting is equivariant to scaling
if fitting to data points $(x_i,y_i)$ and $(\lambda x_i,y_i)$
results in functions $f(x)$ and $\tilde{f}(x)$
which are related as $f(x)=\tilde{f}(x/\lambda)$ for any $\lambda>0$.
Fitting in which of the following basis functions will be equivariant to scaling?

- [ ] monomials: $1$, $x$, $x^2$
- [ ] Lagrange polynomials: $(x-2)(x-3)$, $(x-1)(x-3)$, $(x-1)(x-2)$
- [ ] exponentials: $e^{-x}$, $1$, $e^x$
- [ ] logarithms: $1$, $\log x$, $(\log x)^2$

## Q9

Suppose that the first derivative of $f(x)=\sin(x)$ is calculated at $x=1$
using a finite difference approximation $\frac{f(x+h)-f(x)}{h}$
for an arbitrarily small $h>0$.
What is the best relative error you expect to achieve from a calculation
with double precision?

- [ ] $1$
- [ ] $10^{-8}$
- [ ] $10^{-16}$

## Q10

How many bits are used to represent a number in the IEEE double precision
arithmetic?

## Q11

In the context of function approximation using a polynomial interpolant,
what are the advantages of Chebyshev points over equidistant points?

- [ ] the degree of the polynomial grows slower with the number of points
- [ ] smaller error for the same number of points
- [ ] lower algorithmic complexity of evaluating the Lagrange polynomial

## Q12

Runge's function is an example of

- [ ] a smooth function for which the polynomial interpolation using equidistant
  points leads to an exponential growth of the infinity norm error
- [ ] a basis function equivariant to translation
- [ ] a continuous function with a discontinuous first derivative

## Q13

What is the maximum absolute value of a Chebyshev polynomial $T_{n+1}(x)$
in the range $[-1, 1]$?

- [ ] $1$
- [ ] $2^{n+1}$
- [ ] $1 / 2^{n+1}$
- [ ] $n+1$


