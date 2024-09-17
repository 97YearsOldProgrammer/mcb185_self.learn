# deathsave rule
# d20 
# <10 failure >10 success
# 3 failure with die
# 3 success stable but unconscious
# 1 is 2 failure
# 20 have one health and revived
# Find probability of die stabilizes and revive

import random
import math
import sys

print(f'47deathsaves.py\nThis is p value for deathsaves game')
print()

f = 0 # fail
w = 0 # win
l = 0 # loop
d = 0 # death
s = 0 # stable
r = 0 # revive
limit = 100000

for i in range(limit):
    j = random.randint(1, 20)
    if  f == 3 : 
        d += 1
        l += 1 
        f = 0
        w = 0
    elif  w == 3 : 
        s += 1
        l += 1
        f = 0
        w = 0
    elif  j == 20: 
        r += 1
        l += 1
        f = 0
        w = 0
    if    j < 10  and j != 1 : f += 1
    elif  j >= 10 and j != 20: w += 1
    elif  j == 1 : f += 2

print(f'Probability of death is {d/l*100:.2f}')
print(f'Probability of stable but unconsious is {s/l*100:.2f}')
print(f'Probability of revive is {r/l*100:.2f}')
			
		





