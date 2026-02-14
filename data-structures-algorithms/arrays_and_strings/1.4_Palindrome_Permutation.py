string = input("Enter a String: ").lower()


dict = {}
for i in string:
    if i != " ":
        dict[i] = dict.get(i, 0) + 1

odd = 1
for v in dict.values():
    if v % 2 != 0:
        if odd:
            odd = 0
        else:
            print("Not pallindrome permutation")
            exit()

print("Pallindrome permutation")
