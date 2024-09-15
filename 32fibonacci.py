# First 10 numbers of Fibonacci sequence
# 0 1 1 2 3 5 8 13 21 34

def fib_seq(n):
	if   n == 1:           return 0
	elif n == 2 or n == 3: return 1
	else:				   return fib_seq(n-1) + fib_seq(n-2)

def seq_list(i):		
	if i <= 0: print(error)	
	for i in range(1, i+1):
		print(fib_seq(i))

# seem little bit chubby
# but it worked

seq_list(10)