// Chris Pedro
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13fgnfxdraexpqct222cxnw2nnpf3le3

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

long gcd(long m, long n)
{
  if (m == 0)
    return n;
  return gcd(n % m, m);
}

int main(int argc, char * argv[])
{
  int i, pairs, sum_coprime = 0;
  long rand1, rand2, max = LONG_MAX;
  double percentage_coprime, pi;

  if (argc < 2)
  {
    printf("usage: %s <pairs> [<max_number>]\n", argv[0]);
    return EXIT_FAILURE;
  }

  pairs = atoi(argv[1]);
  if (argc > 2)
    max = atol(argv[2]);

  if (pairs < 10)
  {
    printf("%d must be greater than 10.\n", pairs);
    return EXIT_FAILURE;
  }

  srandomdev();
  for (i = 0; i < pairs; ++i)
  {
    rand1 = (random() % max) + 1;
    rand2 = (random() % max) + 1;

    if (gcd(rand1, rand2) == 1)
      ++sum_coprime;
  }

  percentage_coprime = (double)sum_coprime / pairs;
  pi = sqrt(6/percentage_coprime);

  printf("Generated %d pairs of random numbers between 1 and %ld\n",
    pairs, max);
  printf("Number of co-primes pairs: %d\n", sum_coprime);
  printf("--------------------------\n");
  printf("Pi approximation is %lf\n", pi);

  return EXIT_SUCCESS;
}﻿
