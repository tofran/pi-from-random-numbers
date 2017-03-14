# Buttercak3
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13dyvnbcp2zifrei235jfmyqq2jtdoy304.1489438255537078

Here is a slight modification of your code that makes it many times faster:

import random
import math

# I put these here so you can change them easily
MAX = 9999999 # highest random number
COUNT = 1000000 # number of pairs the program generates

coprime = 0
cofactor = 0

for t in range(COUNT):
    a = random.randint(1, MAX)
    b = random.randint(1, MAX)

    # Euclidean Algorithm - many  times faster than checking every number from 2 to min(a, b)
    while b != 0:
        temp = b
        b = a % b
        a = temp

    # a is now the GCD of the two random numbers
    if a == 1:
        coprime += 1
    else:
        cofactor += 1

print('pi is approx. ' + str(math.sqrt(6 / (coprime / COUNT))))﻿
