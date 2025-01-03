import random
import sys
import math
import toolbox
import mcb185
import itertools
import json
import gzip
import re
import argparse

import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

# creating dictionary for storing data

vcf = {  	'I':	[],
			'II': 	[],
			'III':	[],
			'IV':	[],
			'V':	[],
			'X':	[],		}

# collecting location from vcf file

with gzip.open(arg.vcf, 'rt') as fp:
	for line in fp:
		line = line.split()
		if line == '': break
		head = line[0]
		location = line[1]
		vcf[head].append(location)

# collecting information from gff file

index = []									# for the lower and upper bound

with gzip.open (arg.gff, 'rt') as fp:

	gff = {}
	variant = {}							# where we use number as key, value as variant type
	a = -1

	for line in fp:
		line = line.split()	
		a += 1

		if line[0] == 'I': 
			variant[a]= line[2]				# where we record different types of variant
			bound = (line[3], line[4])
			index.append(bound)

d = dict()

i = int(4014)
n = -1

for lb, ub in index:
						
	n += 1
	lowerbound = int(lb)
	upperbound = int(ub)
		
	if  lowerbound <= i and i <= upperbound: 
		d[variant[n]] = ''

output = [k for k, v in d.items() if not v and k]
output = ','.join(output)
print(f'I\t{i}\t{output}')

		
		

