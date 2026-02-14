str1 = input("Enter a string: ")

len_str = len(str1)
result = ""
i = 0
while i < len_str:
    char = str1[i]
    result += char
    count = 1
    i += 1
    while i < len_str and str1[i] == char:
        count +=1
        i += 1
    result += str(count)

print(result if len_str > len(result) else str1)