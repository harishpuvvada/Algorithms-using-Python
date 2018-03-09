def mergeSortedLists(list1,list2):

    res = []
    i,j = 0,0
    while i < (len(list1)) and j < (len(list2)):
        if list1[i]<list2[j]:
            res.append(list1[i])
            i +=1
        else:
            res.append(list2[j])
            j +=1

    return res + list2[j:] + list1[i:] #appending rest of the elements


list1 = [1,3,5,7,9]
list2 = [2,4,6,8]

print(mergeSortedLists(list1,list2))
