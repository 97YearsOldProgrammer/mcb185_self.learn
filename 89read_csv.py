import random
import sys
import math
import toolbox
import mcb185
import itertools

# kinda interesting about reading csv format
# this one only worked on ~/Code/MCB185/data/primer.csv
# btw we can see the abstract overall frame about this stuff

def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog

path = sys.argv[1]

catalog = read_catalog(path)
print(catalog)
for primer in catalog:
	print(primer['Name'], primer['Description'])

for primer in catalog:
    primer['Tm'] = toolbox.oligont(primer['Sequence'])
print(catalog)