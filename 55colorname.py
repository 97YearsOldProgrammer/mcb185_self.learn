# closest official coloor name

import sys
import math

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
total = R + G + B

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

rgb    	  = []
names  	  = []
colors 	  = []
distances = []

with open(colorfile) as fp:
	for line in fp:	
		parts = line.split('\t')
		name  = parts[0]
		rgb_l = parts[2]
		rgb_s = rgb_l.split(',')
		d = dtc([int(rgb_s[0]), int(rgb_s[1]), int(rgb_s[2])], [R, G, B])
		distances.append(d)
		names.append(name)

mini = distances[0]
for distance in distances[1:]:
	if distance < mini: mini = distance
x = distances.index(mini)


print(f'\nThis is the closest color {names[x]} {R},{G},{B}\n')



	