def quick_sort(a: list[int], left, right):
    if left < right:
        index = partition(a, left, right)
        quick_sort(a, left, index - 1)
        quick_sort(a, index, right)


def partition(a: list[int], left, right):
    pivot = a[(left + right) // 2]
    while left <= right:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1
        if left <= right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
    return left


# def quick_sort(a: list[int]):
#     if len(a) <= 1:
#         return a
#     pivot = a[len(a) // 2]
#     less_than_pivot = [x for x in a if x < pivot]
#     equal_to_pivot = [x for x in a if x == pivot]
#     greater_than_pivot = [x for x in a if x > pivot]

#     return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


def main():
    a = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    quick_sort(a, 0, len(a) - 1)
    print(a)


if __name__ == "__main__":
    main()
