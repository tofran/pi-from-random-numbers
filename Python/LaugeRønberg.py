# Lauge Rønberg
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12tfxnywmbphfuyy04cjd1ovqz3yhz4euo0k.1489445247000689

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
def est(n,random_dist=10**6):
   import random;
   import math;

   cofactor=0;
   coprime=0;
   for i in range(n):
         a,b=random.randint(1,random_dist),random.randint(1,random_dist);
         if gcd(a,b)==1:
             coprime+=1;
         else:
             cofactor+=1;   print(coprime,cofactor);
    print(coprime,cofactor);
    pi=math.sqrt(6*(coprime+cofactor)/coprime);

    return(pi);
