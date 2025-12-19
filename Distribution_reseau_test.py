noeuds = {
    0: (0, 0),
    1: (1, 2),
    2: (3, 4),
    3: (5, 5),
}

arcs = [(0, 1), (1, 2), (2, 3)]

entry = (0, 0)

entry_id = None
for n, coord in noeuds.items():
    if coord == entry:
        entry_id = n
        break

if entry_id is None:
    print("no entry connected")

clients = [(1, 2), (3, 4), (5, 5)]

# algo bfs
# voisin des noeuds a partir des arcs
graph = {n: [] for n in noeuds.keys()}
for n1, n2 in arcs:
    graph[n1].append(n2)
    graph[n2].append(n1)

print("Neighbors graph :", graph)


def bfs(graph, entry_id):
    visited = set()
    queue = [entry_id]
    while queue:
        front = queue.pop(0)
        if front not in visited:
            visited.add(front)
            for neighbor in graph[front]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited


possible_coords = {noeuds[v] for v in dfs_recursive(graph, entry_id)}
# possible_coords = {noeuds[v] for v in bfs(graph, entry_id)}
print("possible coordinates :", possible_coords)

for i, client_coord in enumerate(clients):
    if client_coord in possible_coords:
        print(f"client {i} ok ")
    else:
        print(f"client {i} not okay ")

visited_nodes = bfs(graph, entry_id)
if len(visited_nodes) == len(noeuds):
    print("tous les noeuds connecté")
else:
    not_connected = set(noeuds.keys()) - visited_nodes
    print(f"Noueds non connecté a l'entrée : {not_connected}")
