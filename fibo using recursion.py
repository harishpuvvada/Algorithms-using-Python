"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):

	fib_seq = [0,1,1]


	for i in range(3,position+1):

		el = fib_seq[i-1] + fib_seq[i-2]
		
		fib_seq.append(el)
		
	return fib_seq[position]

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
