def max_heap_sort(arr):
    """ Heap Sort that uses a max heap to sort an array in ascending order
        Complexity: O(n log(n))
    """
    for i in range(len(arr) - 1, 0, -1): #doesn't include 0, (5 to 1)
        max_heapify(arr, i)

        arr[0], arr[i] = arr[i], arr[0] #after
        #print(arr)

def max_heapify(arr, end):
    """ Max heapify helper for max_heap_sort
    """
    last_parent = int((end - 1) / 2)
    #print(last_parent)

    # Iterate from last parent to first
    for parent in range(last_parent, -1, -1):
        current_parent = parent

        # Iterate from current_parent to last_parent
        while current_parent <= last_parent:

            # Find greatest child of current_parent
            child = 2 * current_parent + 1
            #print(child)
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child = child + 1 #compare two childs and make higher valued child as child

            # Swap if child is greater than parent
            if arr[child] > arr[current_parent]:
                arr[current_parent], arr[child] = arr[child], arr[current_parent]

            # If no swap occured, no need to keep iterating
            else:
                break

if __name__ == '__main__':
	import timeit

	array = [12,11,13,5,6,7,2]
	max_heap_sort(array)
	print(array)
