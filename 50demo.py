import sys
import math

# function for mini

def minimum(vals):
	mini = vals[0]
	for val in vales[1:]:
		if val < mini: mini = vals
	return mini

# function for max and mini

def min_max(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

# function for mean

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

# function for entropy

def en(probs):
	h = 0
	for p in probs:
		if  p != 0: h -= p*math.log2(p)
	return h

print(en([0.2, 0.3, 0.45, 0.05, 0]))

def kldiv(P, Q):
	h = 0
	for p, q in zip(P, Q):
		if p != 0 and q != 0:
			h += p*math.log2(p/q)
	return h

prob1 = [0.1, 0,2, 0.35, 0.35]
prob2 = [0.3, 0.2, 0.25, 0.25]
print(kldiv(prob1, prob2))



