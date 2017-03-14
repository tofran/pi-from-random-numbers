// Clark Cox
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z133fhirxta0dzof522xtpxq4mrbtrqjd04.1489437974282317

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

static const uint32_t n = 1000000;

int main()
{
  uint32_t count = 0;

  for(int i = 0; i< n; ++i) {
    double x = arc4random_uniform(n);
    double y = arc4random_uniform(n);
    double distance = sqrt(x * x + y * y);

    if (distance <= n) {
        count++;
    }
  }

  double estimate = 4.0 * count / n;
  printf("pi = %g\n", estimate);


    return 0;
}﻿
