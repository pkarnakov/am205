# AM205 Unit 1: Data Fitting

## [`vander_cond.py`](vander_cond.py)

Constructs the Vandermonde matrix on equidistant points.
Measures the growth rate of the condition number depending on the number of
points.

## [`vander_interp.py`](vander_interp.py)

Performs interpolation using equidistant points by solving a linear system
with the Vandermonde matrix.

## [`cheb_interp.py`](cheb_interp.py)

Performs interpolation using Chebyshev points in the
Lagrange polynomial basis.

## [`lebesgue_const.py`](lebesgue_const.py)

Plots the sum of Lagrange polynomials and computes the Lebesgue constant
for equidistant or Chebyshev points.

## [`spline_tdma.py`](spline_tdma.py)

Constructs a cubic spline with clamped boundary conditions
by solving a tridiagonal system using the TDMA algorithm.

## [`lstsq.py`](lstsq.py)

Performs linear least-squares fitting in the monomial basis
using either the function
`numpy.linals.lstsq` or by solving the normal equations.

## [`nonpoly_fit.py`](nonpoly_fit.py)

Performs linear least-squares fitting in the basis of exponentials.

## [`under_lstsq.py`](under_lstsq.py)

Solves an underdetermined least-squares problem
using either the function
`numpy.linals.lstsq` or by solving the normal equations with a regularizer.

## [`nonlin_lstsq.py`](nonlin_lstsq.py)

Solves the problem of locating a transmitter given distances to beacons
using the Levenberg-Marquardt algorithm from `scipy.optimize.root`.
