class Trie_Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie_Node()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_word

    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def print(self, node=None, depth=0):
        if node is None:
            node = self.root

        print("  " * depth, end="")
        print("|--" * (depth > 0), end="")
        print("*" if node.is_word else "")

        for char, child in node.children.items():
            print("  " * depth, end="")
            print("|--" * (depth > 0), end="")
            print(char)
            self.print(child, depth + 1)


def main():
    trie = Trie()
    trie.insert("DOG")
    trie.insert("CAT")
    trie.insert("CAR")
    trie.insert("CARTOON")
    trie.insert("DOOR")
    trie.insert("MOUSE")
    trie.print()

    print(f"DOG: {trie.search('DOG')}")
    print(f"CARTOO: {trie.search('CARTOO')}")
    print(f"CARTOON: {trie.startswith('CARTOON')}")


if __name__ == "__main__":
    main()
