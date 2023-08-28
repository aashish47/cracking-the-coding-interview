a = input("Enter first string: ")
b = input("Enter second string: ")

if len(a) != len(b):
    print("Not permutations")
    exit()

char_freq = {}
i = 0
while i < len(a):
    char_freq[a[i]] = char_freq.get(a[i], 0) + 1
    i += 1

i = 0
while i < len(b):
    char = b[i]
    if char not in char_freq or char_freq[char] == 0:
        print("Not permutations")
        exit()
    char_freq[char] -= 1
    i += 1

print("Permutations")
