# Monte Carlo
# x y from 0 to 1
# distance to origin
# endless while
# basic formula pi/4 = r/n
# distance to origin = 1 is r

# Checked, work

import math
import random
import sys

r = 0
n = 0

while True:
	x  = random.random()
	y  = random.random()
	d  = math.sqrt(x**2 + y**2)
	n += 1
	if d <= 1: r += 1
	pi = 4*r/n
	print(pi)

	

