from queue import Queue


# Adjacency List


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.neighbours: list[Node] = []


class GraphList:
    def __init__(self) -> None:
        self.nodes: list[Node] = []

    def print_graph(self):
        [
            print(f"{node.data}: {[neighbour.data for neighbour in node.neighbours]}")
            for node in self.nodes
        ]


def dfs(root: Node, visited: set[Node] = set()):
    if not root:
        return

    visited.add(root)
    print(root.data, end=" ")

    [
        dfs(neighbour, visited)
        for neighbour in root.neighbours
        if neighbour not in visited
    ]


def bfs(root: Node):
    if not root:
        return

    q: Queue[Node] = Queue()
    visited: set[Node] = set()
    q.put(root)

    while not q.empty():
        node = q.get()
        if node not in visited:
            visited.add(node)
            print(node.data, end=" ")
            [
                q.put(neighbour)
                for neighbour in node.neighbours
                if neighbour not in visited
            ]


# Adjacency Matrix


class GraphMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, start, end):
        if start >= 0 and end >= 0 and start < self.vertices and end < self.vertices:
            self.adj_matrix[start][end] = 1
            self.adj_matrix[end][start] = 1  # Undirected graph

    def print_graph(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))


def main():
    graph_list = GraphList()

    # Create nodes
    node_0 = Node(0)
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    # Add edges (connections between nodes)
    node_0.neighbours.append(node_1)
    node_0.neighbours.append(node_4)
    node_0.neighbours.append(node_5)
    node_1.neighbours.append(node_3)
    node_1.neighbours.append(node_4)
    node_2.neighbours.append(node_1)
    node_3.neighbours.append(node_2)
    node_3.neighbours.append(node_4)

    # Add nodes to the graph
    graph_list.nodes.append(node_0)
    graph_list.nodes.append(node_1)
    graph_list.nodes.append(node_2)
    graph_list.nodes.append(node_3)

    # graph_list.print_graph()

    print("DFS: ", end=" ")
    dfs(graph_list.nodes[0])
    print()
    print("BFS: ", end=" ")
    bfs(graph_list.nodes[0])

    # graph_matrix = GraphMatrix(5)

    # graph_matrix.add_edge(0, 1)
    # graph_matrix.add_edge(0, 4)
    # graph_matrix.add_edge(1, 2)
    # graph_matrix.add_edge(1, 3)
    # graph_matrix.add_edge(1, 4)
    # graph_matrix.add_edge(2, 3)
    # graph_matrix.add_edge(3, 4)

    # graph_matrix.print_graph()


if __name__ == "__main__":
    main()
