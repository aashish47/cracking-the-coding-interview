str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

mismatch = 0

A = len(str1)
B = len(str2)

if abs(A - B) > 1:
    print(False)

if A == B:
    for i, j in zip(str1, str2):
        if i != j:
            if not mismatch:
                mismatch = 1
            else:
                print(False)
                exit()

if abs(A - B) == 1:
    smaller = min(A, B)
    i = 0
    j = 0

    while i < smaller:
        if str1[i] != str2[j]:
            if not mismatch:
                mismatch = 1
                j += 1
            else:
                print(False)
                exit()
        else:
            i += 1
            j += 1

print(True)
