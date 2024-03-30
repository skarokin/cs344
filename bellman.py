def bellman(G, s):
    dist = {node: float('inf') for node in G}
    dist[s] = 0
    iterations = 0

    # for each edge (u, v), calculate new distance to v. repeat V-1 times
    for _ in range(len(G) - 1):  
        print(f'iteration {iterations}: {dist.values()}')
        iterations += 1
        for node in G:
            for nbr in G[node]:
                if dist[node] != float('inf'):
                    weight = G[node][nbr]
                    dist[nbr] = min(dist[nbr], dist[node] + weight)
    return dist

G = {
    'A': {'B': 4, 'C': -2},
    'B': {'G': -2, 'H': -4},
    'C': {'D': 2, 'F': 1},
    'D': {},
    'E': {'F': -2, 'H': 3},
    'F': {'D': 3},
    'G': {'I': -1},
    'H': {'G': 1},
    'I': {'H': 1},
    'S': {'A': 7, 'C': 6, 'F': 5, 'E': 6}
}

print(bellman(G, 'A'))