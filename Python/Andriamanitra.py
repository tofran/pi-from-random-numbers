# Andriamanitra
# https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12gufha0niverg5004cenmayvilzjlavjs
# https://hastebin.com/raw/ezijehivap

from fractions import gcd
from random import randint
from math import sqrt
from threading import Thread
from time import sleep

# the number of rolls each thread does
NUMBER_OF_TRIES = 25000

# max number a "dice" can roll
MAX_RAND = 1000000

# how many threads to use for simulation
# dice will be rolled THREAD_COUNT*NUMBER_OF_TRIES
# times in total
THREAD_COUNT = 4

def get_n(x):
	for j in range(NUMBER_OF_TRIES):
		progress[x] += 1
		if gcd(randint(1, MAX_RAND), randint(1, MAX_RAND)) == 1:
			results[x] += 1

def get_results():
	rsum = sum(results)
	ntot = sum(progress)
	p = rsum/ntot
	percentage = ntot/(NUMBER_OF_TRIES*THREAD_COUNT)*100
	print()
	print("{0:.1f} % done".format(percentage))
	print("{0}/{1} = {2:.5f}".format(rsum, ntot, p))
	print("pi:", sqrt(6/p))

results = [0]*THREAD_COUNT
progress = [0]*THREAD_COUNT
threads = []

for i in range(THREAD_COUNT):
	process = Thread(target=get_n, args=[i])
	process.start()
	threads.append(process)

# uncomment this to get progress updates during long runs
#while (sum(progress) < 0.95*THREAD_COUNT*NUMBER_OF_TRIES):
#	get_results()
#	sleep(5)

for process in threads:
	process.join()

get_results()
