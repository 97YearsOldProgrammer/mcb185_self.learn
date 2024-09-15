# function solve "n choose k"
#n! / k!( n-k )!

import math

def fac(i):
	j = 1
	for i in range(1, i+1):
		j = j * i
	return j

def nk(n, k):
	if    n < k: print('error')
	else: 
		return ( fac(n)/fac(k)/fac(n-k) )

# Checked,work

print( nk(4,2) )
print( nk(10,9) )
print( nk(1,1) )
print( nk(1,2) )