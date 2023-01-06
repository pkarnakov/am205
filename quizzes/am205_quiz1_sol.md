---
title-meta:
- 'AM205 Quiz 1. Data fitting. Solution'
author-meta:
- 'Petr Karnakov'
---

# AM205 Quiz 1. Data fitting. Solution

## Q1

What is the minimal degree of a polynomial passing through the following
points

x | -1 | 0 | 1 | 2
-|-|-|-|-
y | 1  | 0 | 1 | 4

- [ ] 1
- [X] 2
- [ ] 3
- [ ] 4 or higher

**Answer:** Polynomial $x^2$ passes through the points.

## Q2

How many polynomials of degree $n$ pass through points
$S=\{(x_1,y_1),\ldots,(x_n,y_n)\}$ with distinct $x_1,\ldots,x_n$?

- [ ] zero
- [ ] one
- [X] infinitely many
- [ ] depends on $S$

**Answer:** For any arbitrary value at one extra point, the polynomial of degree $n$ would be unique.

## Q3

Suppose that $f(x)$ is an interpolating spline of degree 5,
i.e. $f(x)$ is a piecewise polynomial of degree 5 in each of $n$ segments
$[x_{i-1}, x_{i}]$ for $i=1,\ldots,n$
and $f(x)$ passes through points $(x_i,y_i)$ for $i=0,\ldots,n$.
In addition, $f(x)$ is required to have 4 continuous derivatives in $[x_0,x_n]$.
How many additional constraints need to be imposed on $f(x)$ to guarantee
its uniqueness?

**Answer:** 4. There are $6n$ parameters, $2n$ interpolation constraints,
  $n-1$ constraints on first derivative, $n-1$ constraints on second derivative,
  $n-1$ constraints on third derivative, and $n-1$ constraints on fourth derivative.

## Q4

Without accounting for the rounding error, which of the following polynomials
interpolates discrete data more accurately?

- [ ] an interpolating polynomial constructed in the monomial basis?
- [ ] an interpolating polynomial constructed in the Lagrange polynomial basis?
- [X] both have the same accuracy

**Answer:** The interpolation problem is solved exactly regardless of the basis
chosen, and the two polynomials coincide.

## Q5

Suppose that $L_i(x),\; i=0,\ldots,n$
represent the Lagrange polynomial basis on points $\{x_i\}$.
What is the degree of $g(x) = x \big(\sum_{i=0}^n{L_i(x)}\big)$?

**Answer:** 1. The sum $\sum_{i=0}^n{L_i(x)}$ is a
polynomial of degree $\leq n$ that evaluates to $1$ at $n+1$ points,
so the sum is identical to $1$, and $g(x)=x$ has degree 1.

## Q6

Which of the following are examples of nonlinear least-squares fitting
problems?

- [ ] fitting a straight line to discrete data
- [ ] fitting a quadratic polynomial *to* discrete data

**Answer:** Both models depend linearly on the parameters, so the fitting
problem is linear in both cases.

## Q7

Interpolating polynomials are often used for function approximation.
Two common choices for the set of interpolation points are
the equidistant points and Chebyshev points.
Which of the two will produce a lower approximation error?

- [ ] equidistant points
- [ ] Chebyshev points
- [X] depends on the function


**Answer:** 
One would expect a lower error using Chebyshev points.
However, this does not hold in general.
Consider $f(x)=0$ perturbed near one Chebyshev point.

![](q7_cheb_equi.pdf)

## Q8

Linear least-squares fitting is equivariant to scaling
if fitting to data points $(x_i,y_i)$ and $(\lambda x_i,y_i)$
results in functions $f(x)$ and $\tilde{f}(x)$
which are related as $f(x)=\tilde{f}(x/\lambda)$ for any $\lambda>0$.
Fitting in which of the following basis functions will be equivariant to scaling?

- [X] monomials: $1$, $x$, $x^2$
- [X] Lagrange polynomials: $(x-2)(x-3)$, $(x-1)(x-3)$, $(x-1)(x-2)$
- [ ] exponentials: $e^{-x}$, $1$, $e^x$
- [X] logarithms: $1$, $\log x$, $(\log x)^2$

**Answer:** Monomials and Lagrange polynomials both span all polynomials of
degree $\leq 2$. Scaling $x$ in a polynomial yields another polynomial.
Exponentials change in a non-linear way, see example in
[Unit 1](https://code.harvard.edu/pages/AM205/public/slides/unit1/#/79).
Under scaling $\lambda x$, powers of the logarithm behave like polynomials under
translation $x+\lambda$.

\clearpage
## Q9

Suppose that the first derivative of $f(x)=\sin(x)$ is calculated at $x=1$
using a finite difference approximation $\frac{f(x+h)-f(x)}{h}$
for an arbitrarily small $h>0$.
What is the best relative error you expect to achieve from a calculation
with double precision?

- [ ] $1$
- [X] $10^{-8}$
- [ ] $10^{-16}$

**Answer:** The error will behave like $h + \epsilon / h$ which is minimized at $h=\sqrt{\epsilon}$.
See [Unit 0](https://code.harvard.edu/pages/AM205/public/slides/unit0/#/20).

## Q10

How many bits are used to represent a number in the IEEE double precision
arithmetic?

**Answer:** 64

## Q11

In the context of function approximation using a polynomial interpolant,
what are the advantages of Chebyshev points over equidistant points?

- [ ] the degree of the polynomial grows slower with the number of points
- [X] smaller error for the same number of points
- [ ] lower algorithmic complexity of evaluating the Lagrange polynomial

**Answer:** The error is generally lower, but the degree and the algorithmic
complexity are the same.

## Q12

Runge's function is an example of

- [X] a smooth function for which the polynomial interpolation using equidistant
  points leads to an exponential growth of the infinity norm error
- [ ] a basis function equivariant to translation
- [ ] a continuous function with a discontinuous first derivative

**Answer:** Translation changes the function in a non-linear way,
not compatible with equivariance to translation. Runge's function is smooth.

## Q13

What is the maximum absolute value of a Chebyshev polynomial $T_{n+1}(x)$
in the range $[-1, 1]$?

- [X] $1$
- [ ] $2^{n+1}$
- [ ] $1 / 2^{n+1}$
- [ ] $n+1$

**Answer:** From the definition $T_{n+1}(x)=\cos{((n+1)\arccos x)}$, the maximum
value is 1.

