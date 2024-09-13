# function that take 3 input parameters & give of the largest one

def max3(a, b, c):
	if 	 a > b and a > c:   print(' "a" is the largest number')
	elif b > a and b > c:   print(' "b" is the largest number')
	elif c > a and c > b:   print(' "c" is the largest number')
	else: 					print('There is no largest number')

# integral test Checked_work
max3(10, 19, 20)
max3(25, 99, 100)
max3(10, 10, 10)

# float test Checked_work
max3(10.5*8.9 ,12.4, 11.3)
max3(99.9*9,100*9.9,99.8*9.9)