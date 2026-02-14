from collections import deque


# Adjaceny List
class Graph_Adj_List:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        # undirected graph
        # if v not in self.graph:
        #     self.graph[v] = []
        # self.graph[v].append(u)

    def print_graph(self):
        for vertex in self.graph:
            # print(f"{vertex}->{'->'.join(map(str, self.graph[vertex]))}")
            print(f"{vertex}: {self.graph[vertex]}")

    def bfs(self, start):
        visited = set()
        q = deque([start])
        while q:
            vertex = q.popleft()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end="->")
                if vertex in self.graph:
                    q.extend(self.graph[vertex])

    def dfs(self, start):
        visited = set()
        self.dfs_helper(start, visited)

    def dfs_helper(self, vertex, visited):
        print(vertex, end="->")
        visited.add(vertex)
        if vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    self.dfs_helper(neighbour, visited)


class Graph_Adj_Matrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        if u >= 0 and u < self.vertices and v >= 0 and v < self.vertices:
            self.matrix[u][v] = 1
        #  undirected graph
        #  self.matrix[v][u] = 1

    def print_graph(self):
        print(end="  ")
        for i in range(self.vertices):
            print(i, end=" ")
        print()
        for i in range(self.vertices):
            print(i, end=" ")
            for j in range(self.vertices):
                print(self.matrix[i][j], end=" ")
            print()

    def bfs(self, start):
        visited = set()
        q = deque([start])

        while q:
            vertex = q.popleft()
            if vertex not in visited:
                print(vertex, end="->")
                visited.add(vertex)
                for neighbour, connected in enumerate(self.matrix[vertex]):
                    if connected and neighbour not in visited:
                        q.append(neighbour)

    def dfs(self, start):
        visited = set()
        self.dfs_helper(start, visited)

    def dfs_helper(self, vertex, visited):
        print(vertex, end="->")
        visited.add(vertex)
        for neighbour, connected in enumerate(self.matrix[vertex]):
            if connected and neighbour not in visited:
                self.dfs_helper(neighbour, visited)


def main():

    graph = Graph_Adj_List()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    print("\nAdjacency List: \n")
    graph.print_graph()
    print("\nBFS: ", end="")
    graph.bfs(0)
    print("\n\nDFS: ", end="")
    graph.dfs(0)

    graph = Graph_Adj_Matrix(6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    print("\n\nAdjacency Matrix: \n")
    graph.print_graph()
    print("\nBFS: ", end="")
    graph.bfs(0)
    print("\n\nDFS: ", end="")
    graph.dfs(0)


if __name__ == "__main__":
    main()
