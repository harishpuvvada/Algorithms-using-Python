

def rev_string(s): #using slice notation
	return s[::-1]

def rev_string(s): #using reversed() function
	return ''.join(reversed(s))

def rev_string(s): #recursion
	if len(s) == 1:
		return s

	return s[-1] + rev_string(s[:-1])



