import sys
import gzip

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1

## for f, n in count.items(): print(f, n)	

#  similar sort comment in python3
## for k in sorted(count): prink(k, count[k])

#  show result of library, interesting
## print(count)

for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)

import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)