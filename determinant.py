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

def matrixDeterminant5(matrix):
    a = matrix[0][0]
    minorA = getMinor(matrix, (0,0))
    detMinorA = matrixDeterminant4(minorA)

    b = matrix[0][1]
    minorB = getMinor(matrix, (0,1))
    detMinorB = matrixDeterminant4(minorB)

    c = matrix[0][2]
    minorC = getMinor(matrix, (0,2))
    detMinorC = matrixDeterminant4(minorC)

    d = matrix[0][3]
    minorD = getMinor(matrix, (0,3))
    detMinorD = matrixDeterminant4(minorD)

    e = matrix[0][4]
    minorE = getMinor(matrix, (0, 4))
    detMinorE = matrixDeterminant4(minorE)

    return a*detMinorA - b*detMinorB + c*detMinorC - d*detMinorD + e*detMinorE

def matrixDeterminant4(matrix):
    a = matrix[0][0]
    minorA = getMinor(matrix, (0,0))
    detMinorA = matrixDeterminant3(minorA)

    b = matrix[0][1]
    minorB = getMinor(matrix, (0,1))
    detMinorB = matrixDeterminant3(minorB)

    c = matrix[0][2]
    minorC = getMinor(matrix, (0,2))
    detMinorC = matrixDeterminant3(minorC)

    d = matrix[0][3]
    minorD = getMinor(matrix, (0,3))
    detMinorD = matrixDeterminant3(minorD)

    return a*detMinorA - b*detMinorB + c*detMinorC - d*detMinorD

def matrixDeterminant3(matrix):
    a = matrix[0][0]
    minorA = getMinor(matrix, (0,0))
    detMinorA = matrixDeterminant2(minorA)

    b = matrix[0][1]
    minorB = getMinor(matrix, (0,1))
    detMinorB = matrixDeterminant2(minorB)

    c = matrix[0][2]
    minorC = getMinor(matrix, (0,2))
    detMinorC = matrixDeterminant2(minorC)

    return a*detMinorA - b*detMinorB + c*detMinorC

def matrixDeterminant2(matrix):
    ad = matrix[0][0] * matrix[1][1]
    bc = matrix[1][0] * matrix[0][1]
    return ad-bc

def matrixDeterminant1(matrix):
    return matrix[0][0]

print("Welcome to the determinant calculator")
print("You can only calculate the determinant of square matrix")
print("The current limit is a 5x5 matrix")
size = ""
while not isinstance(size, int):
    size = input("Enter the size of your matrix ")

    try:
        size = int(size)
    except ValueError:
        print("Must enter a positive integer less than 5")
        size = ""
        continue

    if size < 1 or size > 5:
        print("Must enter a positive integer less than 5")
        size = ""
        continue

correct = "n"

while correct != "y":
    matrix = []
    for row in range(1,size+1):
        columnList = []
        for column in range(1, size+1):
            value = ""
            while not isinstance(value, float):
                value = input(f"Enter the number in row {row}, column {column} ")
                
                try:
                    value = float(value)
                except ValueError:
                    print("Must enter a number")

            if value.is_integer() == True:
                columnList.append(int(value))
            else:
                columnList.append(value)

        matrix.append(columnList)

    print("Your Matrix")
    print("\n".join(["\t".join([str(cell) for cell in rows]) for rows in matrix]))

    correct = input("Is this Matrix correct? (y/n) ").lower()
    if correct == "n":
        print("Restarting Matrix input")

determinant = globals()[f'matrixDeterminant{size}'](matrix) 

print(f"The determinant of the matrix is {determinant}")