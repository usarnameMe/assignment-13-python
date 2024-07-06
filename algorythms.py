from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(graph[vertex] - visited)
    return result



def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex] - visited)
    return result

graph = {
    'A': {'B', 'C', 'D', 'E'},
    'B': {'A', 'F', 'G'},
    'C': {'A', 'K'},
    'D': {'A', 'M'},
    'E': {'A', 'L'},
    'F': {'B', 'H'},
    'G': {'B', 'I'},
    'H': {'F', 'J'},
    'I': {'G', 'J'},
    'J': {'H', 'I', 'Z'},
    'K': {'C', 'N', 'O'},
    'L': {'E', 'R'},
    'M': {'D', 'O'},
    'N': {'K', 'P'},
    'O': {'K', 'M', 'Q'},
    'P': {'N', 'Z'},
    'Q': {'O', 'Z'},
    'R': {'L', 'S', 'T'},
    'S': {'R'},
    'T': {'R'},
    'Z': {'J', 'P', 'Q'}
}

dfs_result = dfs(graph, 'A')
bfs_result = bfs(graph, 'A')

print("DFS:", dfs_result)
print("BFS:", bfs_result)
