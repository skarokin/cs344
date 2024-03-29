import heapq

def dijkstras(G, start):
    '''
    INPUT: adjacency list G, start node
    OUTPUT: array of shortest distance from start to each node
    ALGORITHM:
        initialize distances array
        initialize visited set
        initialize priority queue (explore nodes with shortest distance first to enforce greedy algorithm)
        while pq is not empty:
            pop node with shortest distance from pq
            if distance to node > current shortest distance, skip (no point exploring a longer path)
            for each neighbor of node:
                distance_to_nbr = distance to node + edge weight
                if dsitance_to_nbr < current shortest distance to nbr:
                    update distances array
                    push node to pq
    '''
    distances = [float('inf') for _ in range(len(G))]
    distances[start] = 0
    visited = set()
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for nbr in G[node]:
            distance_to_nbr = dist + G[node][nbr]
            if distance_to_nbr < distances[nbr]:
                distances[nbr] = distance_to_nbr
                heapq.heappush(pq, (distance_to_nbr, nbr))
    return distances

def main():
    G = [
        {1: 4, 2: 1},
        {0: 4, 2: 2, 3: 2},
        {0: 1, 1: 2, 3: 7},
        {1: 5, 2: 8}
    ]

    print(dijkstras(G, 0))

main()
