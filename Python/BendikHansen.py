# Bendik Mihle Hansen
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13tyf455tmczz0t423yvzjr4oujullhh04

import random
import math
from fractions import gcd

intsize = 1000000
a = []
b = []
length = 10000
portion = 0

for i in range(length):
    a.append(random.randint(0 , intsize))
    b.append(random.randint(0 , intsize))

    c = gcd(a[i],b[i])

    if c == 1:
        d = 1
        portion = portion + 1
    else: d = 0

    print(a[i] , b[i] , d)
    i = i+1

pi = math.sqrt(6 /(portion / length))

print("")
print(length , portion)
print ("Pi is" , pi)﻿
