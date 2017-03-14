# Bryan Ng
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z131ff1iazbhvtnpa04cffxwjyezg1joc14
# http://pastebin.com/raw/c9W5dyGa

from random import randint
import math

def gcd(x,y):
	return gcd(b,a%b)

coprime=0
cofactor=0

t=0

while t<10:
	a=randint(1,120)
	b=randint(1,120)
	if gcd(a,b)==1:
		coprime+=1
	else:
		cofactor+=1
	t+=1
print math.sqrt(6/(coprime/(coprime+cofactor)))
