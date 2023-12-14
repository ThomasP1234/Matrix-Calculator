def getMinor(matrix, pos):
    rowIgnore = pos[0]
    columnIgnore = pos[1]
    minor = []
    rowCounter = 0
    for row in matrix:
        if rowCounter == rowIgnore:
            rowCounter += 1
            continue

        columnList = []
        columnCounter = 0
        for column in row:
            if columnCounter == columnIgnore:
                columnCounter += 1
                continue

            columnList.append(column)
            columnCounter += 1

        minor.append(columnList)
        rowCounter += 1

    return minor

def matrixDeterminant(matrix):
    detTopRowMinors = []
    if len(matrix) == 1:
        return matrix[0]
    
    elif len(matrix) == 2:
        ad = matrix[0][0] * matrix[1][1]
        bc = matrix[1][0] * matrix[0][1]
        return ad-bc

    for id in range(len(matrix[0])):
        minor = getMinor(matrix, (0, id))
        detMinor = matrixDeterminant(minor)

        detTopRowMinors.append(detMinor)

    value = 0
    for id, determinant in enumerate(detTopRowMinors):
        if id % 2 != 0:
            determinant = determinant * -1
        value += matrix[0][id] * determinant
    
    return value

print("Welcome to the determinant calculator")
print("You can only calculate the determinant of square matrix")
print("Enter your matrix like this:")
print("""
[1 2] --> 1,2,3,4 or 1, 2, 3, 4
[3 4]
          
[1 2 3]
[4 5 6] --> 1,2,3,4,5,6,7,8,9 or 1, 2, 3, 4, 5, 6, 7, 8, 9
[7 8 9]

etc.""")

correct = ""
while correct != "y":
    matrix = input(":")
    matrix = matrix.replace(" ", "")
    matrix = matrix.split(",")

    size = len(matrix)**0.5
    if size.is_integer() == False:
        print("A determinant can only be found for square matices")
        print("This means that the number of elements in your matrix but be a square number")
        print("Please re-enter your matrix")
        continue

    for id, number in enumerate(matrix):
        try:
            float(number)

            if int(number) == float(number):
                matrix[id] = int(number)
            else:
                matrix[id] = float(number)
        except ValueError:
            print("Your matrix contains values that aren\'t numbers")
            continue

    size = int(size)
    matrix = [matrix[i:i+size] for i in range(0, len(matrix), size)]

    print("Your Matrix")
    print("\n".join(["\t".join([str(cell) for cell in rows]) for rows in matrix]))

    correct = input("Is this Matrix correct? (y/n) ").lower()
    if correct == "n":
        print("Restarting Matrix input")
newDeterminant = matrixDeterminant(matrix)

print(f"The determinant of the matrix is {newDeterminant}")