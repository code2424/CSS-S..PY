import sys
import threading

# Increase the recursion limit and stack size to handle large graphs
sys.setrecursionlimit(3000000)
threading.stack_size(67108864)

def first_dfs(vertex):
    global finishing_time, explored, visit_order, reversed_graph
    explored[vertex] = True
    for neighbor in reversed_graph[vertex]:
        if not explored[neighbor]:
            first_dfs(neighbor)
    visit_order.append(vertex)

def second_dfs(vertex):
    global current_scc_size, explored, original_graph
    explored[vertex] = True
    current_scc_size += 1
    for neighbor in original_graph[vertex]:
        if not explored[neighbor]:
            second_dfs(neighbor)

def kosaraju_scc():
    global finishing_time, explored, visit_order, current_scc_size, original_graph, reversed_graph
    
    # Read the graph from the file
    num_vertices = 875714  # Number of vertices in the graph
    original_graph = {i: [] for i in range(1, num_vertices + 1)}
    reversed_graph = {i: [] for i in range(1, num_vertices + 1)}
    
    try:
        with open('C:\\Users\\chara\\Downloads\\SCC\\SCC.txt', 'r') as f:
            for line in f:
                u, v = map(int, line.split())
                original_graph[u].append(v)
                reversed_graph[v].append(u)
    except FileNotFoundError:
        print("Error: The file 'SCC.txt' was not found.")
        return
    
    # First pass: DFS on reversed graph to calculate finishing times
    explored = {i: False for i in range(1, num_vertices + 1)}
    visit_order = []
    
    for vertex in range(1, num_vertices + 1):
        if not explored[vertex]:
            first_dfs(vertex)
    
    # Second pass: DFS on original graph in the order of decreasing finishing times
    explored = {i: False for i in range(1, num_vertices + 1)}
    scc_sizes = []
    
    while visit_order:
        vertex = visit_order.pop()
        if not explored[vertex]:
            current_scc_size = 0
            second_dfs(vertex)
            scc_sizes.append(current_scc_size)
    
    scc_sizes.sort(reverse=True)
    print(scc_sizes[:20])

if __name__ == '__main__':
    thread = threading.Thread(target=kosaraju_scc)
    thread.start()
