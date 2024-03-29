def toposort(G):
    '''
    INPUT: adjacency list G
    OUTPUT: topological order of nodes in G
    ALGORITHM:
        initialize visited set
        initialize order list
        for each node in G:
            if node not in visited:
                dfs(node)
        after dfs(node) is complete, add node to the order list
        return the reversed order list

    --- this works because the first node to be fully explored (no unvisited edges) is the last node before backtracking ---
    '''
    def dfs(node):
        visited.add(node)
        for nbr in G[node]:
            if nbr not in visited:
                dfs(nbr)
        order.append(node)

    visited = set()
    order = []

    for node in G:
        if node not in visited:
            dfs(node)

    return order[::-1]  # reverse the list to get the correct order

def main():
    G = {
        0: [2, 3],
        1: [4, 5],
        2: [1, 6, 7],
        3: [8, 9],
        4: [5, 10],
        5: [11],
        6: [12],
        7: [1, 13],
        8: [9, 14],
        9: [],
        10: [3, 11],
        11: [12, 14],
        12: [13],
        13: [14],
        14: []
    }

    print(toposort(G))

main()
