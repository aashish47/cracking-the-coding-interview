def bubble_sort(arr: list[int]):
    n = len(arr)
    print(f"\nsize: {n}\n")

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            return

        print(f"After {i + 1} pass: {arr}")


def main():
    arr = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    print(f"\nInitial array: {arr}")
    bubble_sort(arr)
    print(f"\nSorted array: {arr}")


if __name__ == "__main__":
    main()
