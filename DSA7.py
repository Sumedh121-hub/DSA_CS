vertices = ["A", "B", "C", "D", "E", "F"]
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("E", "F")]

n = len(vertices)
index = {v: i for i, v in enumerate(vertices)}

# ----------------- Adjacency Matrix -----------------
matrix = [[0] * n for _ in range(n)]
for u, v in edges:
    matrix[index[u]][index[v]] = 1
    matrix[index[v]][index[u]] = 1

print("ADJACENCY MATRIX")
print("  " + " ".join(vertices))
for i in range(n):
    print(vertices[i], " ", " ".join(str(x) for x in matrix[i]))

# ----------------- Adjacency List -----------------
adj_list = {v: [] for v in vertices}
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

print("\nADJACENCY LIST")
for v in vertices:
    print(v, "->", " -> ".join(adj_list[v]))

# ----------------- BFS using Adjacency List -----------------
def bfs(start):
    visited = {start}
    queue = [start]
    order = []
    while queue:
        vertex = queue.pop(0)
        order.append(vertex)
        for nb in adj_list[vertex]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order

print("BFS:", " -> ".join(bfs("A")))

# ----------------- DFS using Adjacency Matrix -----------------
visited_dfs = [False] * n
dfs_order = []

def dfs(v):
    visited_dfs[v] = True
    dfs_order.append(vertices[v])

    for j in range(n):
        if matrix[v][j] == 1 and not visited_dfs[j]:
            dfs(j)

dfs(index["A"])
print("DFS:", " -> ".join(dfs_order))