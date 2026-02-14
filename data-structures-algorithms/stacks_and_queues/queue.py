class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def add(self, data):
        new_node = Node(data)
        if not self.rear:
            self.rear = new_node
            self.front = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def remove(self):
        if not self.front:
            print("Queue is empty !!")
            return
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

    def peek(self):
        return None if self.front is None else self.front.data

    def isEmpty(self):
        return self.front == None

    def display(self):
        current = self.front
        print()
        print("FRONT")
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print(None)
