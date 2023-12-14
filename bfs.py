graph = {
 'A': set(['B', 'C']),
 'B': set(['A', 'D', 'E']),
 'C': set(['A', 'F']),
 'D': set(['B']),
 'E': set(['B', 'F']),
 'F': set(['C', 'E'])
}

def bfs(start):
    queue = [start]
    levels = {}  # This Dict Keeps track of levels
    levels[start] = 0  # Depth of start node is 0
    visited = set(start)
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbor in neighbours:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                levels[neighbor] = levels[node] + 1
        print(levels)  # print graph level
    return visited

print(str(bfs('A')))  # print graph node
