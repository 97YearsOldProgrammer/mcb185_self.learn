import sys
import math

probs = []
for arg in sys.argv[1:]:
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('error: invalid')
	probs.append(float(arg))

sum = 0
for p in probs: sum += p
if not math.isclose(sum, 1.0):
	sys.exit('error: probs must sum to 1.0')

h = 0
for p in probs: 
	h -= p * math.log2(p)

print(h)