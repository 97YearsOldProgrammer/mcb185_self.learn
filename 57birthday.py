# birthday paradox
# different approach
# list to birthday

import random
import sys

trails  = int(sys.argv[1])
days    = int(sys.argv[2])
peoples = int(sys.argv[3])

ps  = []

d 	= int(days)

def bd_creator(n):
	return [0] * n

for j in range(trails):
	z = 0
	bds = bd_creator(days)
	for people in range(peoples):
		if z != 1: x = random.randint(0, (days-1) )
		else:	   break
		bds[x] += 1
		for bd in bds:
			if bd == 2:
				ps.append(1)
				z = 1
				break

total = len(ps)
print(f'The probability for {peoples} people to share the same birthday is {total/trails}\n')
