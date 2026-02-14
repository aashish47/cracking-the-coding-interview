class Node:
    def __init__(self, data) -> None:
        self.data: int = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            print("Linked List empty !!")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        prev = self.head
        current = prev.next

        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print("Node not found !!")

    def display(self):
        if not self.head:
            print("Linked List empty !!")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)
