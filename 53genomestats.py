import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []
n       = 0

# extract data
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		n += 1
		words = line.split()
		if words[2] != feature: continue
		ini = int(words[3])
		end = int(words[4])
		lengths.append(end - ini + 1)

# count
count = 0
for length in lengths:
	count += 1
print(f'This is the total {count}')

# maxi mini
mini = lengths[0]
maxi = lengths[0]
for length in lengths:
	if length < mini: mini = length
	if length > maxi: maxi = length
print(f'This is {mini}, {maxi}')

# mean value
total = 0
x     = len(lengths)
for i in range(x):
	total += lengths[i]
print(f'This is the mean {math.ceil(total/count)}')

# sd
mean = math.ceil(total/count)
tota = 0
for i in range(x):
	devi  = mean - lengths[i]
	tota += devi ** 2 

print(f' This is the sd {int(math.sqrt(tota/count))}')

# median
level  = sorted(lengths)
n_med  = int(count)
med_od = (n_med - 1)
med_ev = int(n_med / 2)


if   (count -1 ) % 2 == 0: 
	print(f'This is the median {int(level[int((med_od) /2 + 1)])}')
elif       count % 2 == 0:      
	print(f'This is the median {int((level[med_ev] + level[med_ev - 1])/2)}')