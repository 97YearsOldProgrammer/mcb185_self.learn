 # position weight matrices (PWMs)
# TRANSFAC format
# output as JSON

import sys
import gzip
import json

with gzip.open(sys.argv[1], 'rt') as fp:
	name = None
	Json = []
	pwm  = []
	name_check = []

""" mostly the idea is similar to read fasta file from MCB185 like prof.Ian did """
""" i just learned and copied the idea, did a similar version of it """

	while True:
		line = fp.readline()
		if not line: break
		line = line.strip()

		if line.startswith('ID'): 
			name = line[2:len(line)]
			name_check.append(name)

		if line.startswith('//') and line.endswith('//'):
			d1 = dict()
			d1['id']  = name
			d1['pwm'] = pwm
			Json.append(d1)
			pwm = []
			
		if line.endswith('.0') and (line.startswith('0') or line.startswith('1') ):
			line   = line.split() 							# turn the line into list of strings
			d      = dict()								    # open dictionary for store data
			d['A'] = line[1]
			d['T'] = line[2]
			d['C'] = line[3]
			d['G'] = line[4]
			pwm.append(d)


print(json.dumps(Json, indent=4))

# this is worked, checked, final version




