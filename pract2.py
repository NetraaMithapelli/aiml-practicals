# Practical 2: Uninformed Search Algorithms 
# Implement Breadth First Search (BFS) and Depth First Search (DFS) algorithms 
# for solving route-finding or maze navigation problems. Compare their performance based on path length, nodes explored and execution time.

import time

graph = {
    'A' : ['B' , 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

#BFS
def bfs(start, goal):
    queue = [[start]]
    visited = []
    explored = 0

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.append(node)
            explored += 1

        if node == goal:
            return path, explored

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(path + [neighbour])

    return None , explored

#DFS
def dfs(start, goal):
    stack = [[start]]
    visited = []
    explored = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.append(node)
            explored += 1

        if node == goal:
            return path , explored

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(path + [neighbour])

    return None, explored

start = 'A'
goal = 'F'

#BFS Execution
t1 = time.time()
bfs_path, bfs_nodes = bfs(start, goal)
bfs_time = time.time() - t1

#DFS Execution
t2 = time.time()
dfs_path, dfs_nodes = dfs(start, goal)
dfs_time = time.time() - t2

#Display BFS 
print("\nBFS Path : ", bfs_path)
print("BFS Path Length : ", len(bfs_path)-1)
print("BFS Nodes Explored : ", bfs_nodes)
print("BFS Time  : ", bfs_time)

#Display DFS 
print("\nDFS Path : ", dfs_path)
print("DFS Path Length : ", len(dfs_path)-1)
print("DFS Nodes Explored : ", dfs_nodes)
print("DFS Time  : ", dfs_time)

