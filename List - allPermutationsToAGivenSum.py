def subset_sum(numbers, target, partial=[]):
    print(partial)
    s = sum(partial)

    if(s == target):
        print("sum of ",partial,"=",target)

    if s>= target:
        return

    for i in range(len(numbers)):
        print("iteration",i)
        n = numbers[i]
        rest = numbers[i+1:]
        subset_sum(rest,target,partial + [n])

if __name__ == "__main__":
    subset_sum([3,9,8,4,5,7,10],15)

#Outputs:
#sum([3, 8, 4])=15
#sum([3, 5, 7])=15
#sum([8, 7])=15
#sum([5, 10])=15
