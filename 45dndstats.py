# dndstats
# 3 six-sided dice
# range 3-18
# mean = 10.5

import random
import math
import sys

print(f'45dndstats.py\nThis is D&D stats roll')
print()

# 3D6 Checked, work

print(f'3D6')

stats = 0

for i in range(3):
	r = random.randint(1, 6)
	stats += r
print(stats)
print()

# 3D6r1 re-roll any 1s 
# Checked, work

print(f'3D6 with 1 reroll')

stats = 0

for i in range(4):
	r = random.randint(1, 6)
	if 	  i <= 3: stats += r
	elif  i == 4: stats -= r 
print(stats)
print()

# 3D6x2 take max
# Checked, work

print(f'3D6 twice for max')

stats = 0

for i in range(3):
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	if r1 > r2: stats += r1
	if r2 > r1: stats += r2
print(stats)
print()

# 4D6d1 drop lowest die
# Checked, should be work

print(f'4D6 with dropping lowest')

stats = 0
min   = math.inf

for i in range(4):
	r 	   = random.randint(1,6)
	stats += r
	if r < min: min = r
print(stats-min)
print()


	



