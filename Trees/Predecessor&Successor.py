
'''
    5
   / \
  3   6
 / \   \
2   4   7

'''

def predecessor(root, node): # to find predecessor of a given node and root
    pred = None
    while root:
        if node.val > root.val:
            pred = root
            root = root.right
        else:
            root = root.left
    return pred

def successor(root, node): # to find successor of a given node and root
    succ = None
    while root:
        if node.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ
