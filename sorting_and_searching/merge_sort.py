def merge(a: list[int], start, mid, end):
    leftSize = mid - start + 1
    rightSize = end - mid

    left = []
    right = []

    for i in range(leftSize):
        left.append(a[start + i])
    for j in range(rightSize):
        right.append(a[mid + 1 + j])

    i = 0
    j = 0
    k = start
    while i < leftSize and j < rightSize:
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < leftSize:
        a[k] = left[i]
        k += 1
        i += 1

    while j < rightSize:
        a[k] = right[j]
        k += 1
        j += 1


def merge_sort(a: list[int], start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(a, start, mid)
    merge_sort(a, mid + 1, end)

    merge(a, start, mid, end)


def main():
    a = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    merge_sort(a, 0, len(a) - 1)
    print(a)


if __name__ == "__main__":
    main()
