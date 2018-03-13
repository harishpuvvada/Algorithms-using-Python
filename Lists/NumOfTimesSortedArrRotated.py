#if you find the index of the minimum value then number of elements exist before is the answer
def NumOfTimesRotated(arr,N): #complexity is O(logN)

    start = 0
    end = len(arr) - 1
    while(start <= end):

        mid = (start+end)//2
        next = (mid + 1) % N
        prev = (mid + N - 1) % N  # It worked for just mid +1 and mid -1 too..

        print(start,mid,end)

        if arr[start] <= arr[end]: #array is already sorted
            return start

        if (arr[mid] <= arr[next]) and (arr[mid] <= arr[prev]):
            return arr[mid]

        if (arr[mid] <= arr[end]):  # arr[mid to high] is already sorted then ignore them and see for min in left side
            end = mid - 1

        if (arr[mid] >= arr[start]): #if arr[low to mid] is already sorted then ignore them and see for min in right side
            start = mid + 1

arr = [5,6,8,11,12,15,18,2] #circularly sorted array
print(NumOfTimesRotated(arr,len(arr)))


#Below is a similar but slightly complicated
#you have to find an x element in a circularly sorted array
#https://www.youtube.com/watch?v=uufaK2uLnSI&index=4&list=PL2_aWCzGMAwLPEZrZIcNEq9ukGWPfLT4A
