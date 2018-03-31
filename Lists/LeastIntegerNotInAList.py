'''Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list.

E.g. For a = [1,2,5,7] the least integer not represented by the list or a slice of the list is 4, and if a = [1,2,2,5,7] then the least non-representable integer is 18.'''


import  itertools
sum_list = []
GivenArr = [1, 2, 5, 7]
for L in range(0, len(GivenArr)+1): #for lengths of 0,1,2,3,4
    for subset in itertools.combinations(GivenArr, L): #find different subsets for each length in above line
        sum_list.append(sum(subset)) #write all the sums in to this newlist

new_list = list(set(sum_list)) #finding unique sums
new_list.sort()
print(new_list)
for each in range(0,new_list[-1]+2): #cuz if all possible sums are already possible, then "highest+1" is our ans
    if each not in new_list:
        print(each)
        break
