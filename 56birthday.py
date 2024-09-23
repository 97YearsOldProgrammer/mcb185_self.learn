# birthday paradox
# classroom of students with randomly birthday
# number of daysin calendar and number of people

import random
import sys

trails  = int(sys.argv[1])
days    = int(sys.argv[2])
peoples = int(sys.argv[3])

day  = int(days - 1)
ps   = []

for i in range(trails):
	bds  = []
	z 	 = 0
	n    = -1
	for people in range(peoples):
		n 	 += 1
		x 	 = random.randint(0, days)
		t_bd = x
		if z != 1: bds.append(x)
		else:	   break
		for bd in bds:
			if bd == t_bd and int( bds.index(bd) ) != n:
			 z = 1
			 ps.append(1)
			 break

total = len(ps)
print(f'{total/trails} is the probability for {peoples} people in a classroom to have same birthday')
			



