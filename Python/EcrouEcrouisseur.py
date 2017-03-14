# Ecrou Ecrouisseur
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13tyf455tmczz0t423yvzjr4oujullhh04.1489436792102169

from random import randint as x
from fractions import gcd
(lambda m,n:(6/(sum([gcd(x(1,m),x(1,m))==1 for i in range(n)])/n))**0.5)(1000000,10000)﻿
