#include <algorithm>
#include <cassert>
#include <chrono>
#include <iostream>
#include <random>
#include <vector>

std::vector<double> mul_by_transpose(const std::vector<double>& matr,
                                      size_t n) {
  std::vector<double> res(n * n, 0);
  for (size_t i = 0; i < n; ++i) {
    for (size_t j = 0; j < n; ++j) {
      for (size_t k = 0; k < n; ++k) {
        res[i * n + j] += matr[i * n + k] * matr[j * n + k];
      }
    }
  }
  return res;
}

std::vector<double> get_matrix(size_t n) {
  std::mt19937 gen(2022);
  std::uniform_real_distribution<double> dis(-1, 1);
  std::vector<double> tmp(n * n);
  // Generate random matrix.
  for (size_t i = 0; i < n; ++i) {
    for (size_t j = 0; j < n; ++j) {
      tmp[i * n + j] = dis(gen);
    }
  }
  return mul_by_transpose(tmp, n);
}

std::vector<double> cholesky(std::vector<double> matr, size_t n) {
  std::vector<double> res(n * n, 0);
  auto A = [&](size_t i, size_t j) -> const double& { return matr[i * n + j]; };
  auto L = [&](size_t i, size_t j) -> double& { return res[i * n + j]; };
  // Copy lower triangular part.
  for (size_t i = 0; i < n; ++i) {
    for (size_t j = 0; j < i + 1; ++j) {
      L(i, j) = A(i, j);
    }
  }
  // Compute L.
  for (size_t j = 0; j < n; ++j) {
    L(j, j) = std::sqrt(L(j, j));
    for (size_t i = j + 1; i < n; ++i) {
      L(i, j) /= L(j, j);
    }
    for (size_t k = j + 1; k < n; ++k) {
      for (size_t i = k; i < n; ++i) {
        L(i, k) -= L(i, j) * L(k, j);
      }
    }
  }
  return res;
}

void print(const std::vector<double>& matr, size_t n) {
  for (size_t i = 0; i < n; ++i) {
    for (size_t j = 0; j < n; ++j) {
      printf("%6.3f ", matr[i * n + j]);
    }
    printf("\n");
  }
  printf("\n");
}

int main(int argc, const char **argv) {
  int n = 100;
  if (argc > 2 || (argc == 2 && std::string(argv[1]) == "-h")) {
    std::cerr << "usage: ./cholesky_time [N=" << n << "]" << std::endl;
    return 1;
  }
  if (argc == 2) {
    n = atoi(argv[1]);
  }

  const int count = std::max<int>(1, 10000000 / std::pow<int>(n, 3));

  const auto matr = get_matrix(n);
  std::vector<double> lower;
  volatile double vol;
  const auto tstart = std::chrono::high_resolution_clock::now();
  for (int i = 0; i < count; ++i) {
    lower = cholesky(matr, n);
    vol = lower[0];
  }

  //print(matr, n);
  //print(lower, n);
  //print(mul_by_transpose(lower, n), n);

  printf("n=%d, count=%d\n", n, count);

  const auto tduration = std::chrono::duration_cast<std::chrono::microseconds>(
      std::chrono::high_resolution_clock::now() - tstart);
  const double t_cpp = tduration.count() / 1e3 / count;
  printf("cpp: %.3f ms\n", t_cpp);
  return 0;
}
