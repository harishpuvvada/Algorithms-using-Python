#Below are the three solutions to generate fiboacci series

#Sol 1) just recursion works fine, but takes too much time cuz of recursive calls.
def fibonnaci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonnaci(n-1)+fibonnaci(n-2)

for i in range(111):
    print(fibonnaci(i))


#Sol 2) Using memoization to cache fibo values

fibovalues = {} #global var because every function call, it can use cache values

def mem_fibonnaci(n):
    value = 0
    #return the value if already in cache
    if n in fibovalues:
        return fibovalues[n]

    #if not in cache, compute
    if n==1:
        value =  1 #dont return like before, store it in a val
    elif n==2:
        value =  1
    elif n>2:
        value =  mem_fibonnaci(n-1)+mem_fibonnaci(n-2)

    #place values in cache
    fibovalues[n] = value

    return value


for i in range(111):
    print(mem_fibonnaci(i))

''' Sol 3) Using inbuild python tool - functool '''

from functools import lru_cache

@lru_cache(1000)  #size of cache
def fibonnaci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonnaci(n-1)+fibonnaci(n-2)

for i in range(111):
    print(fibonnaci(i))
