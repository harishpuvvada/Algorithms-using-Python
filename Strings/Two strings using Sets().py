#Hacker rank Two strings problem using set()

import sys

def twoStrings(s1, s2):
    m1 = set(s1) #removes all the duplicates
    m2 = set(s2)
    if set.intersection(m1,m2): #intersection() returns 1 if there is a common lettter
        return "YES"
    return "NO"

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
