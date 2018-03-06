# code to find the order of people how they are going to suicide.
# In "n" people who are going to suicide, here every "mth" person does it.
# you have to find out the order in which people commit suicide.

n=10
m=3
a = []
for i in range(n):
  a.append(i)
s = ""
i = 0
while(len(a)>0):
  i = (i + m - 1)%len(a)
  s += str(a[i]) + " "
  a.remove(a[i])
print (s)
