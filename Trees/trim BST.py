'''
Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree. So, if we get this tree as input:

'''

def trimBST(tree, minVal, maxVal):  # complexity : O(N)

    if not tree:
        return

    tree.left=trimBST(tree.left, minVal, maxVal)
    tree.right=trimBST(tree.right, minVal, maxVal)

    if minVal<=tree.val<=maxVal:
        return tree

    if tree.val<minVal:
        return tree.right

    if tree.val>maxVal:
        return tree.left
