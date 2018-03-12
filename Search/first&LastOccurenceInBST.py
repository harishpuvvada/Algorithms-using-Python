
def firstOccurenceBST(arr,target):
    start = 0
    end = len(arr)-1
    mid =  (end-start)//2

    while(start <= end):
        mid = (end + start) // 2

        if arr[mid] == target: #In a normal BST you return as you find an element.
            result = mid   #Here you have to intialize "end" to mid -1 so that it will check for target at lower indices
            end = mid - 1  # For the last occurence replace this statement with "start = mid+1"

        elif arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

    return result


arr = [2,10,10,10,10,18,20]  #here our function should return 10 at index 2 even though 10 is also present at 3,4 indices

print("In the given array, target is found first at index ",firstOccurenceBST(arr,10))
