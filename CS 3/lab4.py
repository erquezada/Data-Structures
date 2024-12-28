from collections import deque

# Problem 2 Part 1
def dfs(graph, node, target, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    if node == target:
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

# Problem 2 Part 2
def bfs(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Depth-First Search
dfs_found = dfs(graph, 'A', 'F')
print("DFS: Found F:", dfs_found)

# Breadth-First Search
bfs_found = bfs(graph, 'A', 'F')
print("BFS: Found F:", bfs_found)
