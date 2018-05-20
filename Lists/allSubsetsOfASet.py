numbers = [3,4,9]
total = len(numbers)

def subset_sum(numbers, partial=[]):
    global total         # this is how you use global variables inside a function in python
 
    if(len(partial)>= total): # base case - when to stop recursion
        return

    if (len(partial)<= total): 
        print(partial)

    for i in range(len(numbers)): 
        n = numbers[i]
        rest = numbers[i+1:]
        subset_sum(rest,partial + [n])


if __name__ == "__main__":
    subset_sum([1,2,3])
