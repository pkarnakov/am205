#include <cstdio>

int main() {
  double h = 1;

  while (h > 1e-20) {
    if (1 + h == 1) {
      printf("1+h=1:  %.20g\n", h);
    } else {
      printf("1+h!=1: %.20g\n", h);
    }
    h *= 0.1;
  }
}
