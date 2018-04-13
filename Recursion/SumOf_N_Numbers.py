
def sum_rec(n):

    #Base case
    if n==0:
        return 0

    if n>0:
        return n + sum_rec(n-1)
