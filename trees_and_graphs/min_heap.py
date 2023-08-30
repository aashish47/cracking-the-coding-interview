import random


class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        if len(self.heap) > 1:
            self.bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return "heap is empty !!"

        if len(self.heap) == 1:
            return self.heap.pop()

        min = self.heap[0]
        self.heap[0] = self.heap.pop()

        if len(self.heap) > 1:
            self.bubble_down(0)

        return min

    def bubble_up(self, index):
        parent_index = (index - 1) // 2
        # for max heap: self.heap[parent_index] < self.heap[index]
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = (
                self.heap[index],
                self.heap[parent_index],
            )
            index = parent_index
            parent_index = (index - 1) // 2

    def bubble_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        smallest = index

        # for max heap: self.heap[left_child_index] > self.heap[smallest]
        if (
            len(self.heap) > left_child_index
            and self.heap[left_child_index] < self.heap[smallest]
        ):
            smallest = left_child_index

        # for max heap: self.heap[right_child_index] > self.heap[smallest]
        if (
            len(self.heap) > right_child_index
            and self.heap[right_child_index] < self.heap[smallest]
        ):
            smallest = right_child_index

        if index != smallest:
            self.heap[smallest], self.heap[index] = (
                self.heap[index],
                self.heap[smallest],
            )
            self.bubble_down(smallest)


def main():
    min_heap = MinHeap()
    [min_heap.insert(random.randint(0, 50)) for _ in range(20)]
    [print(min_heap.extract_min(), end=" ") for _ in range(21)]


if __name__ == "__main__":
    main()
