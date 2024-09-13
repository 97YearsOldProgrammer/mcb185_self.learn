# phred score 
# formula : Q = - 10log10P

import math

def phred(p):
	if p == 0 or p == 1: print(error)
	q = - 10 * math.log10(p)
	print(q)

# test of p to q
# Checked, work

phred(0.01)
phred(0.001)

# q to p

def prob(q):
	p = 10 ** ( -q/10 )
	print(p)

# test of q to p
# Checked, work

prob(10)
prob(20)