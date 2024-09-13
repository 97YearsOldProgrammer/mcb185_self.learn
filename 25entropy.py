# shannon entroy program
# atcg DNA
# H(x) = - summation * pi *log 2 pi

import math

def se_dna(a, t, c, g):
	sum = a + t + c + g
	ha  = - a/sum * math.log2( a/sum )
	ht  = - t/sum * math.log2( t/sum )
	hc  = - c/sum * math.log2( c/sum )
	hg  = - g/sum * math.log2( g/sum )
	se  = ha + ht + hc + hg
	print(se)

# test on shannon entropy formula
# it should work if the intepretation of shannon entropy formula is correct

se_dna(20, 10 , 10, 26)
se_dna(180, 100, 120, 200)