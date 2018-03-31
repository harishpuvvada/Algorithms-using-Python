numbers = [3,4,9]
total = len(numbers)

def subset_sum(numbers, partial=[]):
    global total

    if (len(partial)<= total):
        print(partial)

    if(len(partial)>= total):
        return

    for i in range(len(numbers)):
        n = numbers[i]
        rest = numbers[i+1:]
        subset_sum(rest,partial + [n])


if __name__ == "__main__":
    subset_sum([1,2,3])
