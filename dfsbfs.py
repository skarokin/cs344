class AdjacencyMatrix:
    # matrix is a 2D list, assume user inputs valid matrix
    def __init__(self, matrix):
        self.matrix = matrix

    def dfs(self, start):
        """
        Algorithm:
            initialize a set to keep track of visited nodes
            initialize a stack to keep track of unexplored nodes
            while stack is not empty:
                set current node as visited
                explore its neighbors:
                    if there is an edge and neighbor has not been visited:
                        mark neighbor for later exploration
        """
        visited = set()
        stack = [start]    # keep track of the node, not the edge
        order_of_visit = ""

        while stack:
            if stack[-1] in visited:
                stack.pop()
                continue
            current = stack.pop()
            visited.add(current)
            order_of_visit += str(current) + "==>"

            # for each column (neighbor) in the current row (node),
            # if there is an edge and neighbor has not been visited, mark for later exploration
            for nbr in range(len(self.matrix[current])):
                if self.matrix[current][nbr] >= 1 and nbr not in visited:
                    print(f"found an edge from {current} to {nbr}")
                    stack.append(nbr)
            print("stack: ", stack)

        return order_of_visit

    def bfs(self, start):
        """
        Algorithm:
            initialize a set to keep track of visited nodes
            initialize a queue to keep track of unexplored nodes
            while queue is not empty:
                set current node as visited
                explore its neighbors:
                    if there is an edge and neighbor has not been visiteD:
                        mark neighbor later exploration
        """
        visited = set()  # Use a set to store unique visited nodes
        queue = [start]
        order_of_visit = ""

        while queue:
            if queue[0] in visited:
                queue.pop(0)
                continue
            current = queue.pop(0)
            visited.add(current)
            order_of_visit += str(current) + "==>"

            for nbr in range(len(self.matrix[current])):
                if self.matrix[current][nbr] >= 1 and nbr not in visited:
                    print(f"found an edge from {current} to {nbr}")
                    queue.append(nbr)
            print("queue: ", queue)

        return order_of_visit

def main():
    adjMatrix = AdjacencyMatrix([
        [0, 1, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 0]
    ])
    print("--- dfs ---")
    print(adjMatrix.dfs(0))
    print("--- bfs ---")
    print(adjMatrix.bfs(0))

main()
