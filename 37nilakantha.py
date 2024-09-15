# nilakantha for pi estimation
# Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...
# though it is not extremely close to 3.14 but pretty munch that's it

def pi_nilak(n):
	pi = 3 + 4/24 - 4/120
	k  = 2 * n
	for i in range(2, n+2, 2):
		pi = pi + 4/( (2+k)*(3+k)*(4+k) ) 
		for j in range(2, n, 2):
			pi = pi - 4/( (4+k)*(5+k)*(6+k) )
	return pi

print(pi_nilak(15))
print(pi_nilak(5))
print(pi_nilak(100))
print(pi_nilak(10000))

# another approach

def math_nilak(n):
	pi = 3
	for f in range(1, n, 1):
		pi = pi + 4 * (-1) ** (f+1) / (2*f * (2*f+1) * (2*f+2))
	return pi

math_nilak(1)





