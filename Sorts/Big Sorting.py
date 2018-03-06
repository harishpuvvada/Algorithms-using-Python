# Sample Input
# 6 This is length of array
# 31415926535897932384626433832795
# 1
# 3
# 10
# 3
# 5

# Sample Output 0
# 1
# 3
# 3
# 5
# 10
# 31415926535897932384626433832795

import sys

def SortingBigIntegers(arr):
    arr.sort(key = lambda x: (len(x), x))
    return arr

n = int(input().strip())
unsorted = []
unsorted_i = 0

for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

arr=SortingBigIntegers(unsorted)
for i in arr:
    print(i)
