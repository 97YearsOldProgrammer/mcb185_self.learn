# All pythagorean triples
# sides a and b less than 100
# Checked, work 

import math

n     = 99
count = 0

for a in range(1, n+1):
	for b in range(1, n+1):
		for c in range(1, n + 100):
			i = c**2
			x = a**2 + b**2 
			if c % 1 == 0 and math.isclose(i, x) and a <= b: 
				print(a, b, c)
				count += 1 

print(count)

