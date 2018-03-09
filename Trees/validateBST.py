# Time:  O(n)
# Space: O(h)
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf")) #float("-inf") gives lowest negative value

    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True

        return low < root.val and root.val < high \
               and self.isValidBSTRecu(root.left, low, root.val) \
               and self.isValidBSTRecu(root.right, root.val, high)
    #Note: \ is used to escape characters that otherwise have a special meaning like - new line,..etc


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    sol = Solution() #Solution Instance
    print (sol.isValidBST(root))
