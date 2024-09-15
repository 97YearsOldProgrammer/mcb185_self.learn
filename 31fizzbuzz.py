# i 1 - 100
# i/3 show Fizz
# i/5 show Buzz

import math

for i in range (1, 101, 1):
	if   i % 3 == 0: print('Fuzz')
	elif i % 5 == 0: print('BUzz')
	else           : print(i)

# this should work, checked