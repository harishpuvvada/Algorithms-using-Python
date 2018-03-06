#--------- output no of edges to be removed for converting tree in to forest with even no of nodes in each tree --------

# You are given a tree (a simple connected graph with no cycles). The tree has  N nodes numbered from  1 to  N and is rooted at node 1.
#
# Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of nodes
#
# Input Format
#
# The first line of input contains two integers  N and M. N  is the number of nodes, and M is the number of edges.
# The next M lines contain two integers U(i) and V(i) which specifies an edge of the tree.
#
# Constraints:
# 2<=N<=100
#
# Note: The tree in the input will be such that it can always be decomposed into components containing an even number of nodes.
#
# Output Format
#
# Print the number of removed edges.
#
# Sample Input
#
# 10 9
# 2 1
# 3 1
# 4 3
# 5 2
# 6 1
# 7 2
# 8 6
# 9 8
# 10 8
# Sample Output
#
# 2
#

class Node(object):
    def __init__(self):
        self.parent = None
        self.size = 1

    def add_parent(self,p):
        self.parent = p
        while p is not None:
            p.size +=1
            p = p.parent

if __name__ == '__main__':
    N, E = map(int, input().split())  #splits the first line of the input and saves as N- no.of nodes as 10 and E- no of edges as 9
    nodes = [Node() for _ in range(N)] # each node is initialized with a size 1 and parent number as None
    for _ in range(E):
        child,parent = map(int,input().split()) #for each edge in E, eg: "2 1" will be stored as child,parent resp
        nodes[child-1].add_parent(nodes[parent-1])

    sum =0 #initialization
    for node in nodes: 
        if node.size % 2 == 0 and node.parent is not None:
            sum = sum + 1
    print(sum)
