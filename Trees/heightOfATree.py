class Node:
    def __init__(self,data,):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(node): #Time complexity is O(number of nodes)

    if node is None:
        return 0
    else:

        right_depth = maxDepth(node.right)
        left_depth = maxDepth(node.left)

    return max(right_depth,left_depth)+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print ("Height of tree is %d" %(maxDepth(root)))
