#returns length of longest increasing sub sequence
#watch this link - https://www.geeksforgeeks.org/longest-increasing-subsequence/
def LIS(arr): #time complexity is O(n^2)
    lis = [1] * len(arr) #initialized with 1 cuz single element itself is a inc sub seq

    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[j] + 1, lis[i])

    #print(lis)

    return max(lis)



#Complexity is O(NlogN)
def lengthOfLIS(nums):
    LIS = []

    def insert(target):
        left, right = 0, len(LIS) - 1
        # Find the first index "left" which satisfies LIS[left] >= target
        while left <= right:
            mid = int(left + (right - left) / 2)
            if LIS[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        # If not found, append the target.
        if left == len(LIS):
            LIS.append(target);
        else:
            LIS[left] = target

    for num in nums:
        insert(num)

    return len(LIS)


arr = [10,22,9,33,21,50,41,60]

print(LIS(arr))
#output is 5

print(lengthOfLIS(arr))
