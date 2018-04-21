'''lambda is a one line anonymous function '''
func = lambda x,y: x if x>y else y  #function to return max of two numbers
print(func(2,7))
#7


from functools import reduce
lis = [1,2,3,4]
print(reduce(lambda x,y:x+y,lis)) #multiplying all elements of a list using FILTER
#10


print(list(map(lambda x: x**2, lis)))  #squaring all elements of a list using MAP
#[1, 4, 9, 16]



print(list(filter(lambda x: x>10,lis))) #filtering elements of a list using FILTER
#[] - empty list


'''

In filter if you guessed 16 to be answer, you are wrong.
These functions dont modify the input lists but create new ones

'''
