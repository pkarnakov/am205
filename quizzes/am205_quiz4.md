---
title-meta:
- 'AM205 Quiz 4. Optimization'
author-meta:
- 'Petr Karnakov'
---

# AM205 Quiz 4. Optimization

## Q1

Suppose that $g:\mathbb{R}\to\mathbb{R}$ is a nonlinear smooth function with a fixed point $\alpha\in\mathbb{R}$, i.e. $g(\alpha)=\alpha$. Which of the following statements are true in general?

- [ ] $g'(\alpha) = 1$
- [ ] $|g'(\alpha)| < 1$
- [ ] $|g'(\alpha)| \leq 1$
- [ ] none of the above

## Q2

Suppose that a sequence $x_k$ converges linearly to $\alpha$. Define $y_k=(x_k - \alpha)^2$. Which of the following statements is true in general?

* [ ] $y_k$ converges linearly to $0$
* [ ] $y_k$ converges superlinearly to $0$

## Q3

Consider a scalar equation $f(x)=0$ with a smooth and strictly convex function $f:\mathbb{R}\to\mathbb{R}$. Which of the following methods are expected to converge **superlinearly**? Assume that the initial guess is chosen sufficiently close to a solution.

- [ ] bisection method
- [ ] Newton's method
- [ ] secant method
- [ ] none of the above

## Q4

Consider a continuous function $f:\mathbb{R}\to\mathbb{R}$.
Which of the following statements are true?

- [ ] if $f$ is coercive on $\mathbb{R}$, then $f$ has a global minimum in $\mathbb{R}$
- [ ] if $f$ has a unique global minimum in $\mathbb{R}$, then $f$ is coercive on $\mathbb{R}$
- [ ] none of the above

## Q5

The function $f(x)=|x|$ defined on $\mathbb{R}$ is

- [ ] coercive
- [ ] convex
- [ ] strictly convex
- [ ] none of the above

## Q6

The Hessian of the function $f(x,y)=x^2 + y^2$ is

* [ ] positive definite
* [ ] negative definite
* [ ] indefinite
* [ ] none of the above

## Q7

To optimize a function $f:\mathbb{R}^n\to\mathbb{R}$, the BFGS algorithm relies on evaluations of

* [ ] the function $f$
* [ ] the gradient $\nabla f$
* [ ] the Hessian $H_f$

## Q8

Recall the Lagrangian function $\mathcal{L}(b,\lambda)=b^Tb+\lambda^T(Ab-y)$ corresponding to an underdetermined linear least squares problem. Assume that $A\in\mathbb{R}^{m\times n}$ has full rank and $m\leq n$. Suppose that this function is minimized using Newton's method with a zero initial guess $b_0=0$ and $\lambda_0=0$. How many iterations would Newton's method need to satisfy $\|\nabla\mathcal{L}\|_2<10^{-5}$ ?

* [ ] one
* [ ] depends on $\|A\|_2$
* [ ] depends on $\|A\|_2$ and $\|y\|_2$


