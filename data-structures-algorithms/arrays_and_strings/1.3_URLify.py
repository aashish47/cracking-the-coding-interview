url = input("Enter a string").strip()

result = ""
space = False
for i in url:
    if i != " ":
        if space:
            result += "%20"
            space = False
        result += i
    elif not space:
        space = True

print(result)
