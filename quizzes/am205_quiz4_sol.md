---
title-meta:
- 'AM205 Quiz 4. Optimization. Solution'
author-meta:
- 'Petr Karnakov'
---

# AM205 Quiz 4. Optimization. Solution

## Q1

Suppose that $g:\mathbb{R}\to\mathbb{R}$ is a nonlinear smooth function with a fixed point $\alpha\in\mathbb{R}$, i.e. $g(\alpha)=\alpha$. Which of the following statements are true in general?

- [ ] $g'(\alpha) = 1$
- [ ] $|g'(\alpha)| < 1$
- [ ] $|g'(\alpha)| \leq 1$
- [X] none of the above

**Answer:** For example, consider a function $\hat g(x) = g(x) + c(x - \alpha)$
which has the same fixed point, but can have an arbitrary derivative depending on $c$.

## Q2

Suppose that a sequence $x_k$ converges linearly to $\alpha$. Define $y_k=(x_k - \alpha)^2$. Which of the following statements is true in general?

* [X] $y_k$ converges linearly to $0$
* [ ] $y_k$ converges superlinearly to $0$

**Answer:** Linear convergence means $\lim_{k\to\infty} |x_{k+1}-\alpha| / |x_{k}-\alpha| = \mu$, where $0 < \mu < 1$.
For $y_k$, we have $\lim_{k\to\infty} |y_{k+1}| / |y_{k}| = \lim_{k\to\infty} (x_{k+1}-\alpha)^2 / (x_{k}-\alpha)^2 = \mu^2$, so $y_k$ converges linearly to $0$.

## Q3

Consider a scalar equation $f(x)=0$ with a smooth and strictly convex function $f:\mathbb{R}\to\mathbb{R}$. Which of the following methods are expected to converge **superlinearly**? Assume that the initial guess is chosen sufficiently close to a solution.

- [ ] bisection method
- [X] Newton's method
- [X] secant method
- [ ] none of the above

## Q4

Consider a continuous function $f:\mathbb{R}\to\mathbb{R}$.
Which of the following statements are true?

- [X] if $f$ is coercive on $\mathbb{R}$, then $f$ has a global minimum in $\mathbb{R}$
- [ ] if $f$ has a unique global minimum in $\mathbb{R}$, then $f$ is coercive on $\mathbb{R}$
- [ ] none of the above

## Q5

The function $f(x)=|x|$ defined on $\mathbb{R}$ is

- [X] coercive
- [X] convex
- [ ] strictly convex
- [ ] none of the above

## Q6

The Hessian of the function $f(x,y)=x^2 + y^2$ is

* [X] positive definite
* [ ] negative definite
* [ ] indefinite
* [ ] none of the above

## Q7

To optimize a function $f:\mathbb{R}^n\to\mathbb{R}$, the BFGS algorithm relies on evaluations of

* [ ] the function $f$
* [X] the gradient $\nabla f$
* [ ] the Hessian $H_f$

## Q8

Recall the Lagrangian function $\mathcal{L}(b,\lambda)=b^Tb+\lambda^T(Ab-y)$ corresponding to an underdetermined linear least squares problem. Assume that $A\in\mathbb{R}^{m\times n}$ has full rank and $m\leq n$. Suppose that this function is minimized using Newton's method with a zero initial guess $b_0=0$ and $\lambda_0=0$. How many iterations would Newton's method need to satisfy $\|\nabla\mathcal{L}\|_2<10^{-5}$ ?

* [X] one
* [ ] depends on $\|A\|_2$
* [ ] depends on $\|A\|_2$ and $\|y\|_2$

**Answer:** Newton's method solves any quadratic optimization problem exactly
after one iteration.

