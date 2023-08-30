class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next: None | Node = None


class HashTable:
    def __init__(self) -> None:
        self.array: list[None | Node] = [None] * 10

    def hash_function(self, key):
        return hash(key) % len(self.array)

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)

        current = self.array[index]

        while current:
            if current.key == key:
                current.value = value
                return
            elif not current.next:
                current.next = new_node
                return
            else:
                current = current.next
        self.array[index] = new_node

    def get(self, key):
        index = self.hash_function(key)
        current = self.array[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

    def remove(self, key):
        index = self.hash_function(key)
        prev = None
        current = self.array[index]

        while current:
            if current.key == key:
                if not prev:
                    self.array[index] = current.next
                else:
                    prev.next = current.next
                return
            current = current.next
        print("Empty hashtable !!")

    def print(self):
        for index in self.array:
            if index:
                current = index
                while current:
                    print(f"key: {current.key} value: {current.value}")
                    current = current.next


def main():
    hash_table = HashTable()

    for i in range(26):
        hash_table.insert(key=chr(97 + i), value=i + 1)

    for i in range(26):
        key = chr(97 + i)
        print(f"key: {key} value: {hash_table.get(key)}")


if __name__ == "__main__":
    main()
