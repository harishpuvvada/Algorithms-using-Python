
'''
Given an integer, create a function which returns the sum of all the individual digits in that integer.
For eg:
if n = 4321, return 4+3+2+1
'''

def sumofdig(n):

    if n==0:
        return 0

    else:
        sum = n%10
        n = n//10
        return sum + sumofdig(n)
