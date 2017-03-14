# Georgi Iliev
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13dyvnbcp2zifrei235jfmyqq2jtdoy304.1489446451083509

from math import sqrt
from fractions import gcd
from random import randrange
print(sqrt(6 / (sum([1 if gcd(randrange(120), randrange(120)) == 1 else 0 for i in range(0, 500)]) / 500)))
