# AM205

Course material for APMTH 205 (numerical methods)
lectured in Fall 2022 at [Harvard SEAS](https://seas.harvard.edu/applied-mathematics/courses).

## Acknowledgements

The material is based on that of previous years lectured by
[Prof. Chris Rycroft](https://people.math.wisc.edu/~chr/am205) (2014-2021),
[Dr. David Knezevic](https://courses.seas.harvard.edu/courses/am205/fall13) (2013),
and Prof. Efthimios Kaxiras (until 2012).

## Lectures

ZIP archive with interactive HTML slides: [am205_2022_slides.zip](https://pkarnakov.github.io/am205/slides/am205_2022_slides.zip)

* Unit 0. Introduction
  ([PDF](https://pkarnakov.github.io/am205/slides/am205_unit0.pdf)
  | [HTML](https://pkarnakov.github.io/am205/slides/unit0)
  | [Examples](examples/unit0))
* Unit 1. Data fitting
  ([PDF](https://pkarnakov.github.io/am205/slides/am205_unit1.pdf)
  | [HTML](https://pkarnakov.github.io/am205/slides/unit1)
  | [Examples](examples/unit1))
* Unit 2. Numerical linear algebra
  ([PDF](https://pkarnakov.github.io/am205/slides/am205_unit2.pdf)
  | [HTML](https://pkarnakov.github.io/am205/slides/unit2)
  | [Examples](examples/unit2))
* Unit 3. Numerical calculus
  ([PDF](https://pkarnakov.github.io/am205/slides/am205_unit3.pdf)
  | [HTML](https://pkarnakov.github.io/am205/slides/unit3)
  | [Examples](examples/unit3))
* Unit 4. Optimization
  ([PDF](https://pkarnakov.github.io/am205/slides/am205_unit4.pdf)
  | [HTML](https://pkarnakov.github.io/am205/slides/unit4)
  | [Examples](examples/unit4))
* Unit 5. Eigenvalue problems and iterative methods
  ([PDF](https://pkarnakov.github.io/am205/slides/am205_unit5.pdf)
  | [HTML](https://pkarnakov.github.io/am205/slides/unit5)
  | [Examples](examples/unit5))

## Homework

* HW0. Introduction
  ([PDF](https://pkarnakov.github.io/am205/homework/am205_hw0.pdf)
  | [Source](homework/hw0_intro))
* HW1. Data fitting
  ([PDF](https://pkarnakov.github.io/am205/homework/am205_hw1.pdf)
  | [Data](https://pkarnakov.github.io/am205/homework/am205_hw1_data.pdf)
  | [Source](homework/hw1_data_fitting))
* HW2. Numerical linear algebra
  ([PDF](https://pkarnakov.github.io/am205/homework/am205_hw2.pdf)
  | [Data](https://pkarnakov.github.io/am205/homework/am205_hw2_data.pdf)
  | [Source](homework/hw2_linear))
* HW3. Numerical calculus
  ([PDF](https://pkarnakov.github.io/am205/homework/am205_hw3.pdf)
  | [Source](homework/hw3_calculus))
* HW4. PDEs, nonlinear equations, optimization
  ([PDF](https://pkarnakov.github.io/am205/homework/am205_hw4.pdf)
  | [Source](homework/hw4_optimization))
* HW5. PDEs, optimization, iterative methods
  ([PDF](https://pkarnakov.github.io/am205/homework/am205_hw5.pdf)
  | [Data](https://pkarnakov.github.io/am205/homework/am205_hw5_data.pdf)
  | [Source](homework/hw5_iter))

## Quizzes

* Quiz 1. Data fitting
  ([PDF](https://pkarnakov.github.io/am205/quizzes/am205_quiz1.pdf)
  | [Solution](https://pkarnakov.github.io/am205/quizzes/am205_quiz1_sol.pdf)
  | [Source](quizzes/am205_quiz1_sol.md))
* Quiz 2. Numerical linear algebra
  ([PDF](https://pkarnakov.github.io/am205/quizzes/am205_quiz2.pdf)
  | [Solution](https://pkarnakov.github.io/am205/quizzes/am205_quiz2_sol.pdf)
  | [Source](quizzes/am205_quiz2_sol.md))
* Quiz 3. Numerical calculus
  ([PDF](https://pkarnakov.github.io/am205/quizzes/am205_quiz3.pdf)
  | [Solution](https://pkarnakov.github.io/am205/quizzes/am205_quiz3_sol.pdf)
  | [Source](quizzes/am205_quiz3_sol.md))
* Quiz 4. Optimization
  ([PDF](https://pkarnakov.github.io/am205/quizzes/am205_quiz4.pdf)
  | [Solution](https://pkarnakov.github.io/am205/quizzes/am205_quiz4_sol.pdf)
  | [Source](quizzes/am205_quiz4_sol.md))

## Gallery

These images have been used to illustrate the material.
The code to generate them is available in [media](media/).
Click on the image to see the relevant slide.

### Unit 0. Introduction

* [`unit0/fd.py`](media/unit0/media/fd.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit0/#/20"><img src="https://pkarnakov.github.io/am205/slides/unit0/media/fd_abs.svg" height=100 alt="fd_abs.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit0/#/23"><img src="https://pkarnakov.github.io/am205/slides/unit0/media/fd_rel.svg" height=100 alt="fd_rel.svg"></a>

### Unit 1. Data fitting

* [`unit1/data.py`](media/unit1/media/data.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/2"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data.svg" height=100 alt="data.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/3"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_piecewise_linear.svg" height=100 alt="data_piecewise_linear.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/4"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_poly.svg" height=100 alt="data_poly.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/5"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_fit1.svg" height=100 alt="data_fit1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/6"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_fit2.svg" height=100 alt="data_fit2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/7"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_fit3.svg" height=100 alt="data_fit3.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/61"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_spline.svg" height=100 alt="data_spline.svg"></a>

* [`unit1/fit_2d.py`](media/unit1/media/fit_2d.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/8"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/fit_2d.svg" height=100 alt="fit_2d.svg"></a>

* [`unit1/monomials.py`](media/unit1/media/monomials.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/16"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/monomials.svg" height=100 alt="monomials.svg"></a>

* [`unit1/lagrange_two.py`](media/unit1/media/lagrange_two.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/22"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/lagrange_two.svg" height=100 alt="lagrange_two.svg"></a>

* [`unit1/runge.py`](media/unit1/media/runge.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/30"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_deg4.svg" height=100 alt="runge_deg4.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/30"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_deg5.svg" height=100 alt="runge_deg5.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/30"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_deg12.svg" height=100 alt="runge_deg12.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/30"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_deg13.svg" height=100 alt="runge_deg13.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/31"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge.svg" height=100 alt="runge.svg"></a>  
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/37"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_cheb_deg4.svg" height=100 alt="runge_cheb_deg4.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/37"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_cheb_deg5.svg" height=100 alt="runge_cheb_deg5.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/37"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_cheb_deg12.svg" height=100 alt="runge_cheb_deg12.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/37"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_cheb_deg13.svg" height=100 alt="runge_cheb_deg13.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/54"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/runge_spline.svg" height=100 alt="runge_spline.svg"></a>

* [`unit1/cheb.py`](media/unit1/media/cheb.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/36"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/cheb.svg" height=100 alt="cheb.svg"></a>

* [`unit1/cheb_conv.py`](media/unit1/media/cheb_conv.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/38"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/cheb_conv.svg" height=100 alt="cheb_conv.svg"></a>

* [`unit1/lebesgue.py`](media/unit1/media/lebesgue.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/46"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/lebesgue_equi_10.svg" height=100 alt="lebesgue_equi_10.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/46"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/lebesgue_cheb_10.svg" height=100 alt="lebesgue_cheb_10.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/47"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/lebesgue_equi_20.svg" height=100 alt="lebesgue_equi_20.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/47"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/lebesgue_cheb_20.svg" height=100 alt="lebesgue_cheb_20.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/48"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/lebesgue_equi_30.svg" height=100 alt="lebesgue_equi_30.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/48"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/lebesgue_cheb_30.svg" height=100 alt="lebesgue_cheb_30.svg"></a>

* [`unit1/data_anim.py`](media/unit1/media/data_anim.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/62"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_anim_poly.gif" height=100 alt="data_anim_poly.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/62"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/data_anim_spline.gif" height=100 alt="data_anim_spline.webm"></a>

* [`unit1/nonpoly_fit.py`](media/unit1/media/nonpoly_fit.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/75"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonpoly_fit_n1.svg" height=100 alt="nonpoly_fit_n1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/75"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonpoly_fit_n2.svg" height=100 alt="nonpoly_fit_n2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/75"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonpoly_fit_n3.svg" height=100 alt="nonpoly_fit_n3.svg"></a>

* [`unit1/invar_anim.py`](media/unit1/media/invar_anim.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/78"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/invar_anim_trans_poly.gif" height=100 alt="invar_anim_trans_poly.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/78"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/invar_anim_trans_exp.gif" height=100 alt="invar_anim_trans_exp.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/79"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/invar_anim_scal_poly.gif" height=100 alt="invar_anim_scal_poly.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/79"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/invar_anim_scal_exp.gif" height=100 alt="invar_anim_scal_exp.webm"></a>

* [`unit1/underlstsq.py`](media/unit1/media/underlstsq.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/89"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/underlstsq_1.svg" height=100 alt="underlstsq_1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/90"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/underlstsq_2.svg" height=100 alt="underlstsq_2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/91"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/underlstsq_3.svg" height=100 alt="underlstsq_3.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/92"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/underlstsq_4.svg" height=100 alt="underlstsq_4.svg"></a>

* [`unit1/nonpoly_fit_abs.py`](media/unit1/media/nonpoly_fit_abs.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/94"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonpoly_fit_abs_basis.svg" height=100 alt="nonpoly_fit_abs_basis.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/94"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonpoly_fit_abs_fit.svg" height=100 alt="nonpoly_fit_abs_fit.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/95"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonpoly_fit_abs_basis_nonlin.svg" height=100 alt="nonpoly_fit_abs_basis_nonlin.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/95"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonpoly_fit_abs_fit_nonlin.svg" height=100 alt="nonpoly_fit_abs_fit_nonlin.svg"></a>

* [`unit1/nonlin_lstsq.py`](media/unit1/media/nonlin_lstsq.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/96"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonlin_lstsq_1.svg" height=100 alt="nonlin_lstsq_1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/114"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonlin_lstsq_2.svg" height=100 alt="nonlin_lstsq_2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit1/#/115"><img src="https://pkarnakov.github.io/am205/slides/unit1/media/nonlin_lstsq_3.svg" height=100 alt="nonlin_lstsq_3.svg"></a>

### Unit 2. Numerical linear algebra

* [`unit2/electric_circuit.py`](media/unit2/media/electric_circuit.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/3"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/electric_circuit.svg" height=100 alt="electric_circuit.svg"></a>

* [`unit2/spring.py`](media/unit2/media/spring.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/7"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/spring.svg" height=100 alt="spring.svg"></a>

* [`unit2/norm_inf.py`](media/unit2/media/norm_inf.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/22"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/norm_inf.svg" height=100 alt="norm_inf.svg"></a>

* [`unit2/unit_circle_norm.py`](media/unit2/media/unit_circle_norm.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/26"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/unit_circle_norm_1.svg" height=100 alt="unit_circle_norm_1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/26"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/unit_circle_norm_2.svg" height=100 alt="unit_circle_norm_2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/26"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/unit_circle_norm_4.svg" height=100 alt="unit_circle_norm_4.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/26"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/unit_circle_norm_inf.svg" height=100 alt="unit_circle_norm_inf.svg"></a>

* [`unit2/householder.py`](media/unit2/media/householder.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/120"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/householder_1.svg" height=100 alt="householder_1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/121"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/householder_angles.svg" height=100 alt="householder_angles.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/126"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/householder_2.svg" height=100 alt="householder_2.svg"></a>

* [`unit2/svd_drawing.py`](media/unit2/media/svd_drawing.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/144"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/svd_drawing.gif" height=100 alt="svd_drawing.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/145"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/svd_drawing.svg" height=100 alt="svd_drawing.svg"></a>

* [`unit2/pca_dataset.py`](media/unit2/media/pca_dataset.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/163"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pca_dataset.svg" height=100 alt="pca_dataset.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/166"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pca_dataset_arrow.svg" height=100 alt="pca_dataset_arrow.svg"></a>

* [`unit2/pcavideo/pcavideo.py`](media/unit2/media/pcavideo/pcavideo.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/168"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_paris.gif" height=100 alt="pcavideo_paris.mp4"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/169"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_paris_first3.gif" height=100 alt="pcavideo_paris_first3.mp4"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/170"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_paris_zero3.gif" height=100 alt="pcavideo_paris_zero3.mp4"></a>  
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/171"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_vietnam.gif" height=100 alt="pcavideo_vietnam.mp4"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/172"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_vietnam_first3.gif" height=100 alt="pcavideo_vietnam_first3.mp4"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/173"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_vietnam_zero3.gif" height=100 alt="pcavideo_vietnam_zero3.mp4"></a>  
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/174"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_sunrise.gif" height=100 alt="pcavideo_sunrise.mp4"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/175"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_sunrise_first3.gif" height=100 alt="pcavideo_sunrise_first3.mp4"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit2/#/176"><img src="https://pkarnakov.github.io/am205/slides/unit2/media/pcavideo/pcavideo_sunrise_zero3.gif" height=100 alt="pcavideo_sunrise_zero3.mp4"></a>

### Unit 3. Numerical calculus

* [`unit3/quad_rect.py`](media/unit3/media/quad_rect.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/2"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/quad_rect.svg" height=100 alt="quad_rect.svg"></a>

* [`unit3/heat_1d.py`](media/unit3/media/heat_1d.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/14"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/heat_1d.svg" height=100 alt="heat_1d.svg"></a>

* [`unit3/heat_1d_time.py`](media/unit3/media/heat_1d_time.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/16"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/heat_1d_time.svg" height=100 alt="heat_1d_time.svg"></a>

* [`unit3/lagrange_blowup.py`](media/unit3/media/lagrange_blowup.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/32"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/lagrange_blowup.svg" height=100 alt="lagrange_blowup.svg"></a>

* [`unit3/legendre.py`](media/unit3/media/legendre.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/44"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/legendre.svg" height=100 alt="legendre.svg"></a>

* [`unit3/legendre_roots.py`](media/unit3/media/legendre_roots.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/46"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/legendre_roots_5.svg" height=100 alt="legendre_roots_5.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/46"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/legendre_roots_10.svg" height=100 alt="legendre_roots_10.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/46"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/legendre_roots_15.svg" height=100 alt="legendre_roots_15.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/46"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/legendre_roots_20.svg" height=100 alt="legendre_roots_20.svg"></a>

* [`unit3/sparsity.py`](media/unit3/media/sparsity.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/59"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/sparsity.svg" height=100 alt="sparsity.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/61"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/sparsity_bc.svg" height=100 alt="sparsity_bc.svg"></a>

* [`unit3/lotka_volterra.py`](media/unit3/media/lotka_volterra.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/65"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/lotka_volterra.svg" height=100 alt="lotka_volterra.svg"></a>

* [`unit3/lambdastab.py`](media/unit3/media/lambdastab.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/95"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/lambdastab_m1.svg" height=100 alt="lambdastab_m1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/95"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/lambdastab_0.svg" height=100 alt="lambdastab_0.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/95"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/lambdastab_1.svg" height=100 alt="lambdastab_1.svg"></a>

* [`unit3/stabregion_euler.py`](media/unit3/media/stabregion_euler.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/102"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/stabregion_euler_forw_rel.svg" height=100 alt="stabregion_euler_forw_rel.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/105"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/stabregion_euler_back_rel.svg" height=100 alt="stabregion_euler_back_rel.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/107"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/stabregion_euler_ode.svg" height=100 alt="stabregion_euler_ode.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/107"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/stabregion_euler_forw.svg" height=100 alt="stabregion_euler_forw.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/107"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/stabregion_euler_back.svg" height=100 alt="stabregion_euler_back.svg"></a>

* [`unit3/stabregion.py`](media/unit3/media/stabregion.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/112"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/stabregion.svg" height=100 alt="stabregion.svg"></a>

* [`unit3/stabregion_fehlberg.py`](media/unit3/media/stabregion_fehlberg.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/121"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/stabregion_fehlberg.svg" height=100 alt="stabregion_fehlberg.svg"></a>

* [`unit3/shooting.py`](media/unit3/media/shooting.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/131"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/shooting.svg" height=100 alt="shooting.svg"></a>

* [`unit3/conic.py`](media/unit3/media/conic.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/144"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/conic_hyper.svg" height=100 alt="conic_hyper.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/145"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/conic_para.svg" height=100 alt="conic_para.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/146"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/conic_ell.svg" height=100 alt="conic_ell.svg"></a>

* [`unit3/advection_exp.py`](media/unit3/media/advection_exp.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/151"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/advection_exp.svg" height=100 alt="advection_exp.svg"></a>

* [`unit3/char_bc.py`](media/unit3/media/char_bc.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/153"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/char_bc_pos.svg" height=100 alt="char_bc_pos.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/153"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/char_bc_neg.svg" height=100 alt="char_bc_neg.svg"></a>

* [`unit3/char_div.py`](media/unit3/media/char_div.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/156"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/char_div.svg" height=100 alt="char_div.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/157"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/char_div_2.svg" height=100 alt="char_div_2.svg"></a>

* [`unit3/grid.py`](media/unit3/media/grid.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/159"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid.svg" height=100 alt="grid.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/162"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_cfl0.svg" height=100 alt="grid_cfl0.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/164"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_cfl1.svg" height=100 alt="grid_cfl1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/165"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_cfl2.svg" height=100 alt="grid_cfl2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/166"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_cfl3.svg" height=100 alt="grid_cfl3.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/168"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_cfl4.svg" height=100 alt="grid_cfl4.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/171"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_cfl5.svg" height=100 alt="grid_cfl5.svg"></a>

* [`unit3/wave.py`](media/unit3/media/wave.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/191"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/wave_energy.svg" height=100 alt="wave_energy.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/191"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/wave_force.gif" height=100 alt="wave_force.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/191"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/wave_signal.gif" height=100 alt="wave_signal.webm"></a>

* [`unit3/sawtooth_mode.py`](media/unit3/media/sawtooth_mode.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/198"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/sawtooth_mode.svg" height=100 alt="sawtooth_mode.svg"></a>

* [`unit3/theta_stab.py`](media/unit3/media/theta_stab.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/200"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/theta_stab.svg" height=100 alt="theta_stab.svg"></a>

* [`unit3/grid_xy.py`](media/unit3/media/grid_xy.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/206"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_xy.svg" height=100 alt="grid_xy.svg"></a>

* [`unit3/grid_xy_flat.py`](media/unit3/media/grid_xy_flat.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/211"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/grid_xy_flat.svg" height=100 alt="grid_xy_flat.svg"></a>

* [`unit3/poisson.py`](media/unit3/media/poisson.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/214"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/poisson_spy.svg" height=100 alt="poisson_spy.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit3/#/215"><img src="https://pkarnakov.github.io/am205/slides/unit3/media/poisson.svg" height=100 alt="poisson.svg"></a>

### Unit 4. Optimization

* [`unit4/bisection.py`](media/unit4/media/bisection.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/8"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/bisection.svg" height=100 alt="bisection.svg"></a>

* [`unit4/linear_prog.py`](media/unit4/media/linear_prog.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/15"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/linear_prog.svg" height=100 alt="linear_prog.svg"></a>

* [`unit4/global.py`](media/unit4/media/global.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/17"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/global_one.svg" height=100 alt="global_one.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/18"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/global_many.svg" height=100 alt="global_many.svg"></a>

* [`unit4/fixed.py`](media/unit4/media/fixed.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/30"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/fixed.svg" height=100 alt="fixed.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/33"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/fixed_log.svg" height=100 alt="fixed_log.svg"></a>

* [`unit4/coercive.py`](media/unit4/media/coercive.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/62"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/coercive_x2y2.svg" height=100 alt="coercive_x2y2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/62"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/coercive_x2my2.svg" height=100 alt="coercive_x2my2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/62"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/coercive_exp.svg" height=100 alt="coercive_exp.svg"></a>

* [`unit4/convex.py`](media/unit4/media/convex.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/65"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/convex_x2y2.svg" height=100 alt="convex_x2y2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/65"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/convex_x2my2.svg" height=100 alt="convex_x2my2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit4/#/65"><img src="https://pkarnakov.github.io/am205/slides/unit4/media/convex_max.svg" height=100 alt="convex_max.svg"></a>

### Unit 5. Eigenvalue problems and iterative methods

* [`unit5/harmonics.py`](media/unit5/media/harmonics.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/5"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/harmonics_1.svg" height=100 alt="harmonics_1.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/5"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/harmonics_2.svg" height=100 alt="harmonics_2.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/5"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/harmonics_3.svg" height=100 alt="harmonics_3.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/5"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/harmonics_4.svg" height=100 alt="harmonics_4.svg"></a>

* [`unit5/multigrid.py`](media/unit5/media/multigrid.py)

  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/88"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/multigrid_jacobi.gif" height=100 alt="multigrid_jacobi.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/88"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/multigrid_sm_jac.svg" height=100 alt="multigrid_sm_jac.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/90"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/multigrid_gs.gif" height=100 alt="multigrid_gs.webm"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/90"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/multigrid_sm.svg" height=100 alt="multigrid_sm.svg"></a>  
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/93"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/multigrid_maxlvl_gs.svg" height=100 alt="multigrid_maxlvl_gs.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/94"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/multigrid_maxlvl_jac.svg" height=100 alt="multigrid_maxlvl_jac.svg"></a>
  <a href="https://pkarnakov.github.io/am205/slides/unit5/#/95"><img src="https://pkarnakov.github.io/am205/slides/unit5/media/multigrid_maxlvl_jac05.svg" height=100 alt="multigrid_maxlvl_jac05.svg"></a>



