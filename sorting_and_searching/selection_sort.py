def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def selection_sort(a: list[int]):
    i = 0
    while i < len(a):
        j = i + 1
        min = i
        while j < len(a):
            if a[j] < a[min]:
                min = j
            j += 1
        if min != i:
            a[i], a[min] = a[min], a[i]
        i += 1


def main():
    a = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    selection_sort(a)
    print(a)


if __name__ == "__main__":
    main()
