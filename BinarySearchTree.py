class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return insert_helper(self.root,new_val)

    def search(self, find_val):
        return search_helper(self.root,new_val)

    def insert_helper(current,new_val):
        if (new_val > current.value):
            insert_helper(current.right,new_val)

        elif(new_val < current.value):
            insert_helper(current.left,new_val)




# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
