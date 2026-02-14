from queue import Queue


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children: list[Node] = []


class Tree:
    def __init__(self) -> None:
        self.root = None

    def build_tree(self):
        q: Queue[Node] = Queue()
        data = input("Enter data: ")
        self.root = Node(data)
        q.put(self.root)
        while not q.empty():
            current = q.get()
            try:
                children = int(input(f"Enter total children for node {current.data}: "))
                for i in range(children):
                    childData = input(
                        f"Enter {current.data} node's child {i + 1} data: "
                    )
                    childNode = Node(childData)
                    current.children.append(childNode)
                    q.put(childNode)
            except ValueError:
                print("Invalid input !! Enter valid integer.")
                exit()

    def print_tree(self):
        if not self.root:
            print("Tree empty !!")
            return
        q: Queue[Node | None] = Queue()
        q.put(self.root)
        q.put(None)
        while not q.empty():
            current = q.get()
            if current:
                print(current.data, end=" ")
                children = current.children
                totalChildren = len(children)
                for i in range(totalChildren):
                    q.put(children[i])
            else:
                if not q.empty():
                    print()
                    q.put(None)


def main():
    tree = Tree()
    tree.build_tree()
    tree.print_tree()


if __name__ == "__main__":
    main()
