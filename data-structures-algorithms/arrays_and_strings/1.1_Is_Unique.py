input = input("Enter a string: ")

print("-----------------------------------------")
print("By sorting")

user_input = sorted(input)

i = 0
while i < len(user_input) - 1:
    if user_input[i] == user_input[i + 1]:
        print("Not unique")
        break
    i += 1

print("unique")


print("-----------------------------------------")
print("By hashmap")


i = 0
dict = {}

while i < len(input) - 1:
    if input[i] in dict:
        print("Not unique")
        exit()
    dict[input[i]] = 1
    i += 1

print("unique")
