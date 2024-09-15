# Triangular Number Calculation

def tri_sum(n):
	sum = 0
	for i in range(n+1):
		sum = sum + i
	print(sum)

# Checked, work

tri_sum(10)
tri_sum(1)
tri_sum(2)

# factorial of a number

def fac_i(n):
	fac = 1
	for i in range(1, n+1):
		fac = fac * i
	print(fac)
s
# Checked, work

fac_i(10)
fac_i(5)
fac_i(3)

# Approximation of euler number

import math

def e_app(n):
	e   = 1
	fac = 1
	for f in range(1, n+1):
		fac = fac * f
		e 	= e + 1/fac

	print(e)

# Checked, work

e_app(1)
e_app(5)
e_app(15)
e_app(100)

# perfect square detector

import math

def is_perf_sq(n):
	root = math.sqrt(n)
	if root % 1 == 0: print(True)
	else:             print(False)

# Checked, work

is_perf_sq(4)
is_perf_sq(14)



