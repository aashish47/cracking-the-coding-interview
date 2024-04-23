def bisect_left(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:  # only differene from bisect_right
            left = mid + 1
        else:
            right = mid - 1
    return left


def bisect_right(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target >= arr[mid]:  # only difference from bisect_left
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    a = [1, 2, 3, 3, 4, 5, 7, 7, 8, 9, 10]
    left = a.copy()
    right = a.copy()
    target = 7
    index_left = bisect_left(a, target)
    index_right = bisect_right(a, target)

    left.insert(index_left, target)
    right.insert(index_right, target)
    print(f"Original    : {a}")
    print(f"Target      : {target}")
    print(f"Index left  : {index_left}")
    print(f"Left insert : {left}")
    print(f"Index right : {index_right}")
    print(f"Right insert: {right}")


if __name__ == "__main__":
    main()
