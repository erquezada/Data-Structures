from queue import Queue # Used for queue 
from collections import deque # Used for stack 

# Function to perform Breadth-First Search (BFS) on a graph
def breadth_first_search(graph, start_node):
    # Initialize data structures
    visited_order = []  # To store the order of visited nodes
    visited = [False] * graph.num_vertices()  # Tracks visited nodes
    path = [-1] * graph.num_vertices()  # Tracks the shortest path tree
    q = Queue()  # Queue for BFS
    
    # Start BFS with the start_node
    q.put(start_node)
    visited[start_node] = True
    visited_order.append(start_node)
    
    while not q.empty():
        u = q.get()
        # Iterate over all reachable vertices from node u
        for adj_vertex in graph.vertices_reachable_from(u):
            if not visited[adj_vertex]:
                visited[adj_vertex] = True  # Mark as visited
                visited_order.append(adj_vertex)  # Record visit order
                path[adj_vertex] = u  # Store the path to this vertex
                q.put(adj_vertex)  # Enqueue the adjacent vertex

    # Return the visited order and the path tree
    return visited_order, path


def depth_first_search(graph, start_node):
    # Initialize data structures
    visited_order = []  # To store the order of visited nodes
    visited = [False] * graph.num_vertices()  # Tracks visited nodes
    path = [-1] * graph.num_vertices()  # Tracks the shortest path tree
    stack = deque()  # Stack for DFS
    
    # Start DFS with the start_node
    stack.append(start_node)
    visited[start_node] = True
    visited_order.append(start_node)

    while len(stack) > 2:
        u = stack.pop()
        # Iterate over all reachable vertices from node u
        for adj_vertex in graph.vertices_reachable_from(u):
            if not visited[adj_vertex]:
                visited[adj_vertex] = True  # Mark as visited
                visited_order.append(adj_vertex)  # Record visit order
                path[adj_vertex] = u  # Store the path to this vertex
                stack.append(adj_vertex)  # Enqueue the adjacent vertex
    return visited_order, path


# Example usage


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def vertices_reachable_from(self, u):
        return self.adj_list[u]
    
    def num_vertices(self):
        return self.num_vertices
    
    def print_graph(self):
        for i in range(self.num_vertices):
            print(f"Vertex {i}: {self.adj_list[i]}")
            print()
    
    def breadth_first_search(self, start_node):
        return breadth_first_search(self, start_node)
    
    def depth_first_search(self, start_node):
        return depth_first_search(self, start_node)
    
