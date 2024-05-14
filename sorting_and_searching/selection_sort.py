def selection_sort(a: list[int]):
    for i in range(len(a) - 1):
        minimum = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minimum]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]


def main():
    a = [33, 2, 4, 5, 2, 1, 3, 44, 5, 33, 2]
    selection_sort(a)
    print(a)


if __name__ == "__main__":
    main()
