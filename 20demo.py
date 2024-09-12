
# 20demo.py by Gong Chen

print ('hellow world') 

print ('hellow,again') # greeting

import math
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type(b), type(c), sep=', ')

def greeting():
	print('hello Gong Chen')

def pythagoras(a,b):
	c = math.sqrt(a**2 + b**2)
	return c

x = pythagoras(3,4)
print(x)

print(pythagoras(1,1))

# Pratice of Unit 2 Calculation

# Area computing formula

def area(a,b):
	c = a*b
	return c 

a = area(2,2) # Checked_work
print(a)

# circumferences

def circum(r):
	pi = math.pi
	circum = 2*pi*r
	return circum

circumtest = circum(5) # Checked_work
print(circumtest)

# converting C to F
def tem(c):
	f = 9/5*c 
	return f

f = tem(100) # Checked_work
print(f)

# I am not doing speed here
# I am not familiar with these stuff

# double-stranded DNA concentration from OD260

def dsDNA(OD260):
	concentration = 50*OD260
	return concentration

concentration = dsDNA(150)
print(concentration)

# Formula to calculate distance of two point in graph

def x_axis(x1,x2):
	x_component = (x1-x2)^2
	return x_component

def y_axis(y1,y2):
	y_component = (y1-y2)^2
	return y_component

def distance(x_component,y_component):
	d = math.sqrt(x_component+y_component)
	return d

# test for distance
# point (4,4) & point (1,1)

d = distance(x_axis(4,1),y_axis(4,1)) #Finally,it worked
print(d)

def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

#boolean function test

c = 1 == 1
print(c)
print(type(c))

# string comparison test

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')	

# Function that determine if a number is a integer

def is_integer(a):
	if type(a) is int: print('This is integer')
	elif type(a) is float: print('This is not integer')

is_integer(11) #Checked, work
is_integer(11.5) #Checked, work

# Whether it is a valid probability

def is_validP(p):
	if p <= 1: print('This is a valid probability')
	elif p > 1: print('This is not a valid probability')

is_validP(0.05) #Checked,work
is_validP(1.05)

# DNA letter ATCG molecular weight

def is_mwDNA(letter):
	if   letter == 'T': print('126.11g.mol^-1')
	elif letter == 'C': print('111.10g.mol^-1')
	elif letter == 'G': print('151.13g.mol^-1')
	elif letter == 'A': print('135.13g.mol^-1')
	else: print(error)

is_mwDNA('T') #Checked,work
is_mwDNA('A')
is_mwDNA('C')
is_mwDNA('G')

# Complement of a DNA letter

def comDNA(dna):
	if 	 dna == 'A': print('T')
	elif dna == 'C': print('G')
	elif dna == 'G': print('C')
	elif dna == 'T': print('A')
	else:            print(error)

comDNA('A') #Checked,work
comDNA('C')
comDNA('G')
comDNA('T')

"""
This is a 
multi-line
comment
"""
