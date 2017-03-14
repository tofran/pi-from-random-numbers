// QuomoZ
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12zt3kqtvngentpx04cj5oxate3ytngaa4

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
    srand(time(NULL));

    int n;
    scanf("%d", &n);

    int in = 0;
    for (int i = 0; i < n; ++i) {
        const double x = rand() / (double)RAND_MAX;
        const double y = rand() / (double)RAND_MAX;
        in += x*x + y*y <= 1;
    }
    printf("Pi is %f\n", 4.0 * (double)((double)in/(double)n) );

    return 0;
}﻿
