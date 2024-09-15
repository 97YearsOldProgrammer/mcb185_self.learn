# Poisson possibility
# n^k * e^-n / k!

import math

def poisson_p(n, k):
	p = (n ** k * math.e ** (-n) / math.factorial(k))
	if   n < 0 or k < 0: print('error')
	elif p < 0 or p > 1: print('This is not possible')
	else:                return p

# Checked, work

print( poisson_p(20,15) )
print( poisson_p(3,5) )

