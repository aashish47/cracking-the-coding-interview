def insertion_sort(a: list[int]):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] >= a[j - 1]:
                break
            else:
                a[j], a[j - 1] = a[j - 1], a[j]


def main():
    a = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    insertion_sort(a)
    print(a)


if __name__ == "__main__":
    main()
