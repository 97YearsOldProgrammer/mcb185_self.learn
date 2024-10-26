import random
import sys
import math
import toolbox
import mcb185
import itertools
import json
import gzip
import re





frequency = {}  # dictionary for counting PFW

a = 0

d1 = {	'A': 0, 
	  	'C': 0, 
	  	'G': 0,
	  	'T': 0 	}

for i in range(14):
	a += 1
	frequency[a] = d1
	
frequency[1]['A'] += 1

print(frequency[1])
