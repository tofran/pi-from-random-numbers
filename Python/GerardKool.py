# Gerard Kool
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13dyvnbcp2zifrei235jfmyqq2jtdoy304.1489446501025016

import math
import random

print('PI = ', math.pi)
def calc_pi_by_rand_int(rand_limit = 120, number_of_tries = 500):
    number_of_coprimes = 0
    for i in range(number_of_tries+1):
        rand1 = random.randrange(1, rand_limit+1, 1)
        rand2 = random.randrange(1, rand_limit+1, 1)
        if math.gcd(rand1, rand2) == 1:
            number_of_coprimes = number_of_coprimes + 1

    calculated_pi = math.sqrt( 6 / (number_of_coprimes / number_of_tries) )
    print( calculated_pi, calculated_pi / math.pi  * 100 )
    return calculated_pi


list = [ calc_pi_by_rand_int(rand_limit = 120, number_of_tries = 500) for _ in range(2000) ]
print('PI = ', math.pi)
print('av = ', sum(list)/len(list) )﻿
