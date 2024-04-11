def bellman(G, s):
    dist = {node: float('inf') for node in G}
    dist[s] = 0
    iterations = 0

    # for each edge (u, v), calculate new distance to v. repeat V-1 times
    for _ in range(len(G) - 1):
        print(f'iteration {iterations}: {dist.values()}')
        iterations += 1
        for node in G:
            print(f'node: {node}')
            for nbr in G[node]:
                print(f'neighbor: {nbr}')
                # we can only update the distance if the node is reachable from the start
                if dist[node] != float('inf'):
                    weight = G[node][nbr]
                    dist[nbr] = min(dist[nbr], dist[node] + weight)
    return dist

G = {
    'A': {'B': 6, 'C': 4, 'D': 5},
    'B': {'E': -1},
    'C': {'B': -2, 'E': 3},
    'D': {'C': -2, 'F': -1},
    'E': {'F': 3},
    'F': {},
}

print(bellman(G, 'A'))
