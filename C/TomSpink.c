// Tom Spink
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13gdtw5xmagebuca22rgpq4toblshqdr
// http://pastebin.com/HEBXDQxw

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_NUMBER      1000
#define COFACTOR        0
#define COPRIME         1

static const char *classification_text[] = {
        "co-factor",
        "co-prime"
};

static int classification_counts[2];

static int gcd_of(int a, int b)
{
        int t;
        while (b != 0) {
                t = b;
                b = a % b;
                a = t;
        }

        return a;
}

static int classify(int a, int b)
{
        if (gcd_of(a, b) == 1) {
                return COPRIME;
        } else {
                return COFACTOR;
        }
}

static int roll(unsigned int *numbers)
{
        numbers[0] = rand() % MAX_NUMBER;
        numbers[1] = rand() % MAX_NUMBER;

        return classify(numbers[0], numbers[1]);
}

int main(int argc, char **argv)
{
        srand(time(NULL));

        unsigned int rolls = 1000;

        if (argc > 1) {
                rolls = atoi(argv[1]);
        }

        unsigned int numbers[2];
        for (unsigned i = 0; i < 1000; i++) {
                int classification = roll(numbers);

                printf("[%u] (%u, %u) => %s\n", i, numbers[0], numbers[1], classification_text[classification]);
                classification_counts[classification]++;
        }

        for (unsigned int i = 0; i < 2; i++) {
                printf("%s => %u\n", classification_text[i], classification_counts[i]);
        }

        double P = (double)classification_counts[COPRIME] / ((double)classification_counts[COFACTOR] + (double)classification_counts[COPRIME]);

        printf("P = 6/(pi^2) => ");
        printf("%lf = 6/(pi^2)\n", P);
        printf("pi = (6/%lf)^0.5 => ", P);

        P = 6 / P;
        printf("pi = (%lf)^0.5 = %lf\n", P, sqrt(P));

        return 0;
}
