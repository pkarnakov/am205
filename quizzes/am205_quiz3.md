---
title-meta:
- 'AM205 Quiz 3. Numerical calculus'
author-meta:
- 'Petr Karnakov'
---

# AM205 Quiz 3. Numerical calculus

## Q1

Newton-Cotes formulas are quadrature rules that

* [ ] are obtained by integrating a polynomial interpolant
* [ ] use Newton's method to find the quadrature weights

## Q2

Consider a quadrature rule $Q(f)=\sum_{k=0}^n w_k f(k)$ to approximate the integral $\int_0^2 f(x)dx$. This rule uses $n+1$ function values at integer points $0,\ldots, n$. However, only the points $0,1,2$ belong to the integration range $[0,2]$. Suppose that the constant weights $w_0,\ldots,w_n$ are chosen to maximize the degree of polynomials on which this quadrature is exact. This implies that the quadrature rule is exact on all polynomials of degree (choose the highest)

* [ ] $2$
* [ ] $3$
* [ ] $n$
* [ ] $n+1$

## Q3

Gauss quadrature using $n+1$ points is exact on all polynomials of degree (choose
the highest)

* [ ] $n$
* [ ] $2n+1$

## Q4

The centered difference approximation $\frac{f(x+h)-f(x-h)}{2h}$ to $f'(x)$ is exact on all polynomials $f(x)$ of degree (choose the highest)

* [ ] 0
* [ ] 1
* [ ] 2
* [ ] 3
* [ ] 4


## Q5

Compare two methods for solving a system of linear ODEs: forward Euler (explicit) and backward Euler (implicit). The backward Euler method

- [ ] has a larger stability region
- [ ] has a higher order of accuracy
- [ ] requires solving a linear system at every time step
- [ ] none of the above

## Q6

Richardson extrapolation applies to an existing numerical method and can be used to

- [ ] increase its order of accuracy
- [ ] estimate its order of accuracy
- [ ] estimate its absolute error
- [ ] none of the above

## Q7

Compare one-step and multistep methods for solving ODEs.  To achieve the same order of accuracy, multistep methods require

* [ ] fewer function evaluations
* [ ] more function evaluations

## Q8

Recall the $\theta$-method for the heat equation.  The method is fully explicit with $\theta=0$ and fully implicit with $\theta=1$.  Which of the following methods are unconditionally stable?

- [ ] Crank-Nicolson
- [ ] $\theta$-method with $\theta=0.25$
- [ ] $\theta$-method with $\theta=0.5$
- [ ] $\theta$-method with $\theta=1$
- [ ] none of the above

## Q9

Examples of hyperbolic equations are

- [ ] advection equation
- [ ] heat equation
- [ ] Poisson equation
- [ ] wave equation
- [ ] none of the above


## Q10

Recall the central difference method $\frac{U_j^{n+1} - U_j^n}{\Delta t} + c \frac{U_{j+1}^{n} - U_{j-1}^n}{2 \Delta x} = 0$ for the advection equation. Even if $c\Delta t/\Delta x$ is small, the method cannot be used in practice for the following reasons:

- [ ] does not satisfy the CFL condition
- [ ] unconditionally unstable
- [ ] requires two boundary conditions


