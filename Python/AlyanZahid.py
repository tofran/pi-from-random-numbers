# Alyan Zahid aka 4l13n
# Edited by Andriamanitra
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13dyvnbcp2zifrei235jfmyqq2jtdoy304.1489444232426104
# https://gist.github.com/4l13n/e7eba83e63b4294fc62156bb707d134f
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z13dyvnbcp2zifrei235jfmyqq2jtdoy304.1489447370464978
# https://gist.github.com/Andriamanitra/648971aa58e091e8d7339746a32238f3

import random
import math
def func(rolls):
	# you only need to keep track of one variable
	a=0
	for i in range(rolls):
		x=random.randint(1,100)
		y=random.randint(1,100)
		if x<y:
			# switch x and y around so larger one is always x :)
			x, y = y, x
		# use y for upper bound of range because it's the largest
		# number both x and y can be divisible by
		for j in range(2, y+1):
			# if both x and y are divisible by integer larger than 2
			# we have coprime
			if x%j==0 and y%j==0:
				a+=1
				# simply break here to get out of for-loop since
				# we only need to find one common divisor
				break
	b=rolls-a
	p=float(b/rolls)
	q=math.sqrt(6/p)
	print q
func(100)
