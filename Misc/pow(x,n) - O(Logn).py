#check out: https://www.youtube.com/watch?v=wAyrtLAeWvI

def pow(x,n): #Complexity is O(logn)

    if n==0:
        return 1

    elif n%2==0:
        y = pow(x,n/2)
        return y*y

    else:
        return x * pow(x,n-1)



print(pow(2,3))
