"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

def summaryRanges(arr):
    summary = []
    
    if len(arr) == 1:         # base condition
        return [str(arr[0])]

    i = 0

    while (i < len(arr)):
        temp = ""
        start = str(arr[i])

        while (i < len(arr)-1) and (arr[i+1] == arr[i] + 1):  #to iterate through the nums which increase by 1
            i += 1

        end = str(arr[i])

        if(start == end):
            temp = start
        else:
            temp = start + "-->" + end

        summary.append(temp)
        i = i+1

    return summary

arr = [0,1,2,4,5,7]

print(summaryRanges(arr))
