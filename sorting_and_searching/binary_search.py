def binary_search_recursively(a: list[int], low: int, high: int, num: int):
    if low > high:
        return -1

    mid = (low + high) // 2

    if num > a[mid]:
        return binary_search_recursively(a, mid + 1, high, num)
    elif num < a[mid]:
        return binary_search_recursively(a, low, mid - 1, num)
    else:
        return mid


def binary_search(a: list[int], num):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if num > a[mid]:
            low = mid + 1
        elif num < a[mid]:
            high = mid - 1
        else:
            return mid
    return -1


def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 3
    index_recursion = binary_search_recursively(a, 0, len(a) - 1, x)
    index_iteration = binary_search(a, x)
    print(
        f"{x} found at index {index_recursion} via recursion"
        if index_recursion != -1
        else "not found"
    )
    print(
        f"{x} found at index {index_iteration} via iteration"
        if index_iteration != -1
        else "not found"
    )


if __name__ == "__main__":
    main()
