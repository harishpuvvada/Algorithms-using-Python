"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.

function flatten(input){
}

Example:

Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""


def flatten_rec(input):

    flatList = []

    def makelist(lis):
        for el in lis:
            if type(el) == list:
                makelist(el)
            else:
                flatList.append(el)

    makelist(input)

    return flatList



input = [2, 1, [3, [4, 5], 6], 7, [8]]
print(flatten_rec(input))
