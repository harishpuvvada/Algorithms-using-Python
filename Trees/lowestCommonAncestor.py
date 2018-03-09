# From GeeksandGeeks
# Python program to find LCA of n1 and n2 using one traversal of Binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# This function returns pointer to LCA of two given values n1 and n2
# This function assumes that n1 and n2 are present in Binary Tree
def findLCA(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's value
    if root.value == n1 or root.value == n2:
        return root

    # Look for values in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one value is present in once subtree and other is present in other.
    # So this root is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    if left_lca is not None:
        return left_lca
    else:
        return right_lca



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ", findLCA(root, 4, 5).value)
print("LCA(4,6) = ", findLCA(root, 4, 6).value)
print("LCA(3,4) = ", findLCA(root, 3, 4).value)  #we have to use .value since function is returning "Nodes"
print("LCA(2,4) = ", findLCA(root, 2, 4).value)
