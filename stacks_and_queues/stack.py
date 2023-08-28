class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
            return
        prev_top = self.top
        self.top = new_node
        new_node.next = prev_top

    def pop(self):
        if not self.top:
            print("Stack Empty !!")
            return
        self.top = self.top.next

    def isEmpty(self):
        return self.top == None

    def peek(self):
        return None if self.top == None else self.top.data

    def display(self):
        current = self.top
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print(None)
