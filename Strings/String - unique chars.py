#check if string has all unique chars
def uniq(s):
	if len(list(set(s))) == len(s):
		return True
	else:
		return False


uniq('abbcde');
uniq('abcd');


#return all the unique chars
def uniq(s):
	seen = []
	for char in s:
		if char not in seen:
			seen.append(char)

	return ''.join(seen)


#return false if there are duplicates, else return true
def is_unique(input):
  char_seen = []
  for char in input:
    if char in char_seen:
      return False
    char_seen.append(char)
  return True