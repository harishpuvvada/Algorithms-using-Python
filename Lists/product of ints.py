'''
Given a list of integers, write a function that will return a list, in which for each index the element will be the product of all the integers except for the element at that index

For example, an input of [1,2,3,4] would return [24,12,8,6] by performing [2×3×4,1×3×4,1×2×4,1×2×3]
'''

def index_prod(lst):

    # Create an empty output list
    output = [None] * len(lst)

    # Set initial product and index for greedy run forward
    product = 1
    i = 0

    while i < len(lst):


        # Set index as cumulative product
        output[i] = product

        # Cumulative product
        product *= lst[i]

        # Move forward
        i +=1

        print("output", output)


    # Now for our Greedy run Backwards
    product = 1

    # Start index at last (taking into account index 0)
    i = len(lst) - 1

    print("----")

    # Until the beginning of the list
    while i >=0:


        # Same operations as before, just backwards
        output[i] *= product
        product *= lst[i]
        i -= 1
        print("output", output)

    return output



index_prod([1,2,3,4])
