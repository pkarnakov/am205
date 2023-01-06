---
title-meta:
- 'AM205 Quiz 2. Numerical linear algebra. Solution'
author-meta:
- 'Petr Karnakov'
---

# AM205 Quiz 2. Numerical linear algebra. Solution

## Q1

Which of the vector norm axioms are violated for the $p$-norm if $0<p<1$?

- [ ] absolute homogeneity
- [X] triangle inequality
- [ ] positive definiteness
- [ ] none of the above

## Q2

The product of two upper triangular matrices is an upper triangular matrix.

- [X] true
- [ ] false

## Q3

Consider a matrix $A\in\mathbb{R}^{n\times n}$ and vector $b\in\mathbb{R}^n$. Assume that an LU factorization of $A$ is known. What is the complexity of solving the linear system $Ax=b$ using that LU factorization?

- [ ] $\mathcal{O}(n)$
- [X] $\mathcal{O}(n^2)$
- [ ] $\mathcal{O}(n^3)$
- [ ] none of the above

## Q4

Let $L_j$ be an elementary elimination matrix from one step of the LU factorization algorithm for a square matrix $A$. Which of the following statements are correct in general for any $A$? The matrix $L_j$ is 

- [X] invertible
- [X] lower triangular
- [ ] orthogonal
- [X] sparse
- [ ] none of the above

**Answer:** The matrix is not orthogonal since its inverse is obtained by
negating the elements below the diagonal, which is different from its transpose.

## Q5

Suppose that a square matrix $A$ has a Cholesky factorization $A=LL^T$, where $L$ is a square invertible lower triangular matrix. Which of the following statements are correct in general for any $L$? The matrix $A$ is

- [ ] lower triangular
- [X] positive-definite
- [X] symmetric
- [ ] none of the above

## Q6

Which of the following factorizations of a square matrix are unique?

- [ ] LU
- [ ] QR
- [X] none of the above

## Q7

Suppose that $F$ is a Householder reflector. Which of the following statements are correct in general?

- [X] $F$ is orthogonal
- [X] $F^2=I$
- [ ] none of the above

## Q8

Suppose that $Q$ is an orthogonal matrix and $Q=U\Sigma V^T$ is its singular value decomposition. Which of the following statements are correct in general?

- [X] $\Sigma$ is diagonal
- [X] $\Sigma$ is invertible
- [X] $\|\Sigma\|_2=1$
- [ ] none of the above

**Answer:** For any $Q$, $\|\Sigma\|_2=\|Q\|_2$. Since $Q$ is orthogonal, $\|Q\|_2=1$.

## Q9

Consider a matrix $A\in\mathbb{R}^{n\times n}$ and vector $b\in\mathbb{R}^n$. Which of the following factorizations, once known, reduce the complexity of solving the linear system $Ax=b$ to $\mathcal{O}(n^2)$?

- [X] LU
- [X] QR
- [X] SVD
- [X] Cholesky
- [ ] none of the above

**Answer:**

* $A=LU$, solve $Ly=b$, $Ux=y$
* $A=QR$, solve $Qy=b$, $y=Q^Tb$, $Rx=y$
* $A=U\Sigma V^T$, solve $Uy = b$, $y=U^T b$, $\Sigma V^T x=y$, $V^Tx=\Sigma^{-1}y$, $x=V\Sigma^{-1}y$
* $A=L L^T$ is a type of LU

