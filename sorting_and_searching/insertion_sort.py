def insertion_sort(a: list[int]):
    sorted_array = 0
    while sorted_array < len(a) - 1:
        j = sorted_array + 1
        key = a[j]
        j = j - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        sorted_array += 1


def main():
    a = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    insertion_sort(a)
    print(a)


if __name__ == "__main__":
    main()
