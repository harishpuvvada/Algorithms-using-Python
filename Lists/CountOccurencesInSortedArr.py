#for this question we use "first&last occurences function" in search repo.

def firstORLastOccurenceBST(arr,target,flag):
    start = 0
    end = len(arr)-1
    mid =  (end-start)//2

    while(start <= end):
        mid = (end + start) // 2

        if arr[mid] == target: #In a normal BST you return as you find an element.
            result = mid   #Here you have to intialize "end" to mid -1 so that it will check for target at lower indices
            if flag == 0:
                end = mid - 1  # For the first occurence
            else:
                start = mid + 1 # For the last occurence
        elif arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

    return result



def countOccurences(arr,target): #complexity is O(logN)
    lowestIdx = firstORLastOccurenceBST(arr,target,0)
    highestIdx = firstORLastOccurenceBST(arr,target,1)

    NumOfOccurences = highestIdx - lowestIdx + 1

    return NumOfOccurences


arr = [2,10,10,10,10,18,20]  #sorted array

print("In the given array, target is found ",countOccurences(arr,10), "times")
