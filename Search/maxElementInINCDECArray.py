def maxIncDec(arr):
    #print(arr)
    start = 0
    end = len(arr)-1
    mid = (end-start)//2
    #print("start ",start," end ",end, "mid ", mid)

    if start > end:
        print("inside 1")   # if indexes go out of bounds
        return

    if len(arr) == 1:
        print("inside 2")  #if there is one element
        return arr[0]

    if len(arr) == 2:    # if there are two elements
        return max(arr)

    elif arr[mid] < arr[mid+1] and arr[mid-1] < arr[mid]:
        return maxIncDec(arr[mid+1:])

    elif arr[mid] > arr[mid+1] and arr[mid-1] > arr[mid]:
        return maxIncDec(arr[start:mid])

    elif arr[mid] > arr[mid+1] and  arr[mid] > arr[mid-1]:
        return arr[mid]


arr = [8, 10, 20, 3, 2, 1]

print(maxIncDec(arr))
