def bubble_sort(a: list[int]):
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def main():
    a = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    bubble_sort(a)
    print(a)


if __name__ == "__main__":
    main()
