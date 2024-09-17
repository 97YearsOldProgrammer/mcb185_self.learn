# saving throw of D&D
# 20
# DC 5, 10, 15 

import random
import math
import sys

print(f'46savingthrows.py\nThis is probability for saving throws with 5, 10, 15 DC')
print()

r   = random.randint(1,20)
limit = 100000

dc1 = 5 #DC5

pn1 = 0
tn1 = 0
for i in range(limit):
	r    = random.randint(1, 20)
	tn1 += 1
	if r >= dc1: pn1 += 1

pa1 = 0
ta1 = 0
for i in range(limit):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	ta1 += 1
	if r1 >= dc1 or r2 >= dc1: pa1 += 1

pd1 = 0
td1 = 0
for i in range(limit):
	r1  = random.randint(1, 20)
	r2  = random.randint(1, 20)
	td1+= 1
	if r1 >= dc1 and r2 >= dc1: pd1 += 1

dc2 = 10 #DC10

pn2 = 0
tn2 = 0
for i in range(limit):
	r    = random.randint(1, 20)
	tn2 += 1
	if r >= dc2: pn2 += 1

pa2 = 0
ta2 = 0
for i in range(limit):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	ta2 += 1
	if r1 >= dc2 or r2 >= dc2: pa2 += 1

pd2 = 0
td2 = 0
for i in range(limit):
	r1  = random.randint(1, 20)
	r2  = random.randint(1, 20)
	td2+= 1
	if r1 >= dc2 and r2 >= dc2: pd2 += 1

dc3 = 15 #DC5

pn3 = 0
tn3 = 0
for i in range(limit):
	r    = random.randint(1, 20)
	tn3 += 1
	if r >= dc3: pn3 += 1

pa3 = 0
ta3 = 0
for i in range(limit):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	ta3 += 1
	if r1 >= dc3 or r2 >= dc3: pa3 += 1

pd3 = 0
td3 = 0
for i in range(limit):
	r1  = random.randint(1, 20)
	r2  = random.randint(1, 20)
	td3+= 1
	if r1 >= dc3 and r2 >= dc3: pd3 += 1


print(f'\t DC=5\t DC=10\t DC=15')
print(f'nm\t{pn1/tn1*100: .2f}\t{pn2/tn2*100: .2f}\t{pn3/tn3*100: .2f}')
print(f'ad\t{pa1/ta1*100: .2f}\t{pa2/ta2*100: .2f}\t{pa3/ta3*100: .2f}')
print(f'dad\t{pd1/td1*100: .2f}\t{pd2/td2*100: .2f}\t{pd3/td3*100: .2f}')
print()





