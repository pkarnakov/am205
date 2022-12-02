#include <cfenv>
#include <cmath>
#include <cstdio>
#include <string>

// Directive to allow changing the floating point environment.
#pragma STDC FENV_ACCESS ON

const char* ModeToString(int mode) {
  return mode == FE_TONEAREST    ? "TONEAREST"
         : mode == FE_DOWNWARD   ? "DOWNWARD"
         : mode == FE_UPWARD     ? "UPWARD"
         : mode == FE_TOWARDZERO ? "TOWARDZERO"
                                 : "";
}

void Test() {
  // Qualifier `volatile` prevents evaluation of operations with c1,c3,c5
  // at compile time, not affected by rounding mode.
  volatile float c1 = 1;
  volatile float c3 = 3;
  volatile float c5 = 5;
  printf("%s\n", ModeToString(fegetround()));
  printf("    acosf(-1) = %.12f\n", acosf(-c1));
  printf("    1/3       = %.12f\n", c1 / c3);
  printf("    5/3       = %.12f\n", c5 / c3);
}

int main() {
  Test();

  fesetround(FE_DOWNWARD);
  Test();

  fesetround(FE_UPWARD);
  Test();
}
