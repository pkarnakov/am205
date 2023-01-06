---
title-meta:
- 'AM205 Quiz 2. Numerical linear algebra'
author-meta:
- 'Petr Karnakov'
---

# AM205 Quiz 2. Numerical linear algebra

## Q1

Which of the vector norm axioms are violated for the $p$-norm if $0<p<1$?

- [ ] absolute homogeneity
- [ ] triangle inequality
- [ ] positive definiteness
- [ ] none of the above

## Q2

The product of two upper triangular matrices is an upper triangular matrix.

- [ ] true
- [ ] false

## Q3

Consider a matrix $A\in\mathbb{R}^{n\times n}$ and vector $b\in\mathbb{R}^n$. Assume that an LU factorization of $A$ is known. What is the complexity of solving the linear system $Ax=b$ using that LU factorization?

- [ ] $\mathcal{O}(n)$
- [ ] $\mathcal{O}(n^2)$
- [ ] $\mathcal{O}(n^3)$
- [ ] none of the above

## Q4

Let $L_j$ be an elementary elimination matrix from one step of the LU factorization algorithm for a square matrix $A$. Which of the following statements are correct in general for any $A$? The matrix $L_j$ is 

- [ ] invertible
- [ ] lower triangular
- [ ] orthogonal
- [ ] sparse
- [ ] none of the above

## Q5

Suppose that a square matrix $A$ has a Cholesky factorization $A=LL^T$, where $L$ is a square invertible lower triangular matrix. Which of the following statements are correct in general for any $L$? The matrix $A$ is

- [ ] lower triangular
- [ ] positive-definite
- [ ] symmetric
- [ ] none of the above

## Q6

Which of the following factorizations of a square matrix are unique?

- [ ] LU
- [ ] QR
- [ ] none of the above

## Q7

Suppose that $F$ is a Householder reflector. Which of the following statements are correct in general?

- [ ] $F$ is orthogonal
- [ ] $F^2=I$
- [ ] none of the above

## Q8

Suppose that $Q$ is an orthogonal matrix and $Q=U\Sigma V^T$ is its singular value decomposition. Which of the following statements are correct in general?

- [ ] $\Sigma$ is diagonal
- [ ] $\Sigma$ is invertible
- [ ] $\|\Sigma\|_2=1$
- [ ] none of the above

## Q9

Consider a matrix $A\in\mathbb{R}^{n\times n}$ and vector $b\in\mathbb{R}^n$. Which of the following factorizations, once known, reduce the complexity of solving the linear system $Ax=b$ to $\mathcal{O}(n^2)$?

- [ ] LU
- [ ] QR
- [ ] SVD
- [ ] Cholesky
- [ ] none of the above


