class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def build_tree(self):
        return self.build_tree_recursive()

    def build_tree_recursive(self):
        data = input("Enter data: ").strip()
        if not data:
            return None
        root = Node(data)

        choice = input(f"Do you want to enter data to {data} node's left? y/n ")
        if choice == "y":
            root.left = self.build_tree_recursive()
        choice = input(f"Do you want to enter data to {data} node's right? y/n ")
        if choice == "y":
            root.right = self.build_tree_recursive()

        return root


def in_order(root: Node | None):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)


def pre_order(root: Node | None):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)


def post_order(root: Node | None):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=" ")


def main():
    btree = BinaryTree()
    root = btree.build_tree()
    print("Inorder:", end=" ")
    in_order(root)
    print()
    print("Preorder:", end=" ")
    pre_order(root)
    print()
    print("Postorder:", end=" ")
    post_order(root)
    print()


if __name__ == "__main__":
    main()
