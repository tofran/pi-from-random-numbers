# Саша Крикун
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12gdziwksf1x5tp004cjz5hvm2tj1qpejo

import random
from fractions import gcd
from decimal import Decimal
from math import sqrt
from math import pi
import os

maxval = 120
attempts = 0.0
suc = 0.0
while 1:
 attempts += 1
 a=round(random.random()*maxval+.5)
 b=round(random.random()*maxval+.5)
 suc += gcd(a,b)==1
 x = suc/attempts
 if x==0: x+=1
 piex = sqrt(6/x)
 if attempts %100000 == 0:
  os.system('cls')
  print "Attempts = ", '%.E' % Decimal(attempts), ", Pi =", piex, "Error = ", '%.G' % Decimal(abs(1-piex/pi)*100), '%'﻿
