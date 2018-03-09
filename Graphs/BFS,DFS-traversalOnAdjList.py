graph = {'A': set(['B', 'C', 'F']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['A', 'C', 'E'])}


def dfs_harish(graph,startnode):
    visited = set()
    stack = [startnode]
    while stack:
        node = stack.pop() # This line is the only difference between DFS and BFS. popping the last element
        if node not in visited:
            visited.add(node)
            for adjnode in graph[node]:
                if adjnode not in visited:  # adding all the adjacent nodes of the current node to the stack if not in visited
                    stack.append(adjnode)
    return visited

print(dfs_harish(graph, 'B'))



def bfs_harish(graph,startNode):
    visited = set()
    queue = [startNode]

    while queue:
        node = queue.pop(0) # This line is the only difference between DFS and BFS. popping the element at index 0
        if node not in visited:
            visited.add(node)
            for adjnode in graph[node]:
                if adjnode not in visited:
                    queue.append(adjnode)
    return visited



print(bfs_harish(graph, 'B'))
