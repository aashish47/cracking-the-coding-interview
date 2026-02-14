rows = int(input("Enter total rows: "))
columns = int(input("Enter total columns: "))


def printMatrix():
    for row in matrix:
        print(row)


matrix = [
    [int(input(f"Enter element for row {i+1}, column {j+1}: ")) for j in range(columns)]
    for i in range(rows)
]

print()
printMatrix()
print()

# to store the positions of zero elements
zero = []

for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == 0:
            zero.append([row, column])

#  to keep track of which rows and columns have already been zeroed
zeroRow = []
zeroColumn = []

for z in zero:
    row = z[0]
    column = z[1]
    if row not in zeroRow:
        for i in range(rows):
            matrix[i][column] = 0
    if column not in zeroColumn:
        for j in range(columns):
            matrix[row][j] = 0
    zeroRow.append(row)
    zeroColumn.append(column)

printMatrix()
