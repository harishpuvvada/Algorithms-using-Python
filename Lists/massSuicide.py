# code to find the order of people how they are going to suicide.
# List 'a' people who are going to suicide. Eevery "mth" person jumps one after another.
# you have to find out the order in which people commit suicide.


a = range(0,10)
m=3

s = ""
i = 0

while(len(a)>0):
	i = (i + m - 1)%len(a)
	s += str(a[i]) + " "
	a.remove(a[i])
	print (s)
