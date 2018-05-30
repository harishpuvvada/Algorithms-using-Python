def segregate0and1(arr, size): '''Time complexity is O(n)'''
    # Initialize left and right indexes
    left, right = 0, size-1

    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1

        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
            right -= 1

        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Exchange arr[left] and arr[right]
        if left < right:
            arr[left] = 0   #instead of swap, we can just assign 0 and 1 here
            arr[right] = 1
            left += 1        #since value at this index is now okay, we can inc/dec them
            right -= 1

    return arr

arr = [0, 1, 0, 1, 1, 1]
arr_size = len(arr)
print("Array after segregation")
print(segregate0and1(arr, arr_size))
