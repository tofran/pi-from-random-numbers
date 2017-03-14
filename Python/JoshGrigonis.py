# Josh Grigonis aka jgrigonis
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12zupb40zqtezt3022zylmj4xydepxs4.1489469952230239
# https://gist.github.com/jgrigonis/f5f2f8b4358ed7111e27c66bbc8c63f3

import math
import random
from fractions import gcd


def die_roll(sides):
    return random.randint(1, sides)

def are_coprime(a, b):
    return gcd(a, b) == 1

def distance(x):
    y = math.sqrt(6.0 / x)
    return abs(math.pi - y)

ITERATIONS = 50000
DIE_SIDES = 1*10**100

coprimes = 0
total = 0
closest = 4
for x in range(ITERATIONS):
    if are_coprime(die_roll(DIE_SIDES), die_roll(DIE_SIDES)):
        coprimes += 1
    total += 1
    x = coprimes * 1.0 / total
    # as we get closer to pi, we print out the value
    if x > 0:
        z = distance(x)
        if z < closest:
            closest = z
            print(math.sqrt(6.0 / x))

x = coprimes * 1.0 / total

print(math.sqrt(6.0 / x))
