# Alex Walters
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12ngjwzvoymw10md22ptp44porwx1rqk04
# https://gist.github.com/tritium21/5e91edf00a07abc61ba45b8ed719103e

# Run with python py_for_pi_day.py [number of rounds] [upper limit on random number]
# Python 3.5+
import math
import random
import sys


def main(rounds, limit):
    print(rounds, "Rounds")
    print(limit, "Sides")
    print()
    cp = 0
    cf = 0
    for _ in range(rounds):
        if math.gcd(random.randint(1, limit), random.randint(1, limit)) != 1:
            cf += 1
        else:
            cp += 1
    prob = float(cp) / float(rounds)
    pi = math.sqrt(6 / prob)
    error = round(math.fabs(pi - math.pi)*100, 4)
    print(cp, "Coprimes")
    print(prob, "Probability ({}/{})".format(cp, rounds))
    print()
    print(pi, "\u03C0\u2248\u221A(6/{})".format(cp))
    print(math.pi, "\u03C0 from C runtime (for reference)")
    print("{}% Error.".format(error))

if __name__ == "__main__":
    rounds = 500
    limit = 120
    try:
        rounds = int(sys.argv[1])
        limit = int(sys.argv[2])
    except IndexError:
        pass
    main(rounds, limit)
