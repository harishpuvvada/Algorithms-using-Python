"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array,low,high):
    if(low<high):
        pIndex = partition(array,low,high)
        quicksort(array,low,pIndex-1)
        quicksort(array,pIndex+1,high)

    return array

def partition(array,low,end):
    pivot = array[end] #selecting the right most element as pivot
    pIndex = low
    i = low
    while(i<end): #so that it wont compare with the last element which is the pivot
        if(array[i] <= pivot):
            array[pIndex],array[i] = array[i],array[pIndex]
            pIndex = pIndex + 1
        i=i+1
    array[pIndex],array[end] = array[end],array[pIndex]
    return pIndex

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test,0,9)
