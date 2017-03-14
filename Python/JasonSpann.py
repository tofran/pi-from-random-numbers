# Jason Spann
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13pgfb5plmqvfg2k23tsjnikkb5exeit04

from random import randint
from fractions import gcd
from math import sqrt
coprime = 0
for i in range(0, 500):
  if gcd(randint(1, 120), randint(1, 120)) == 1:
    coprime += 1
print (sqrt(6 / (coprime / 500)))﻿
