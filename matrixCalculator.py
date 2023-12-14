class GetMatrix:
    def sanitise(self, matrix):
        matrix = matrix.replace(" ", "")
        matrix = matrix.split(",")

        size = len(matrix)**0.5
        if size.is_integer() == False:
            print("A determinant can only be found for square matices")
            print("This means that the number of elements in your matrix but be a square number")
            print("Please re-enter your matrix")
            return (0, "0")

        for id, number in enumerate(matrix):
            try:
                float(number)

                if int(number) == float(number):
                    matrix[id] = int(number)
                else:
                    matrix[id] = float(number)
            except ValueError:
                print("Your matrix contains values that aren\'t numbers")
                return (0, "0")

        size = int(size)
        matrix = [matrix[i:i+size] for i in range(0, len(matrix), size)]

        print("Your Matrix:")
        print("\n".join(["\t".join([str(cell) for cell in rows]) for rows in matrix]))

        return (matrix, "1")


    def message(self):
        print("Welcome to the determinant calculator")
        print("You can only calculate the determinant of square matrix")
        print("Enter your matrix like this:")
        print("[1 2] --> 1,2,3,4 or 1, 2, 3, 4")
        print("[3 4]")
        print()
        print("[1 2 3]")
        print("[4 5 6] --> 1,2,3,4,5,6,7,8,9 or 1, 2, 3, 4, 5, 6, 7, 8, 9")
        print("[7 8 9]")
        print()
        print("etc.")


    def get(self):
        self.message()

        correct = ""
        while correct != "y":
            matrix = input(":")
            matrix, correct = self.sanitise(matrix)
            if correct == "0":
                continue

            correct = input("Is this Matrix correct? (y/n) ").lower()
            if correct == "n":
                print("Restarting Matrix input")
        
        return matrix

class Minor:
    def getMinor(self, matrix, pos):
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

class Determinant(Minor):
    def matrixDeterminant(self, matrix):
        detTopRowMinors = []
        if len(matrix) == 1:
            return matrix[0]
        
        elif len(matrix) == 2:
            ad = matrix[0][0] * matrix[1][1]
            bc = matrix[1][0] * matrix[0][1]
            return ad-bc

        for id in range(len(matrix[0])):
            minor = self.getMinor(matrix, (0, id))
            detMinor = self.matrixDeterminant(minor)

            detTopRowMinors.append(detMinor)

        value = 0
        for id, determinant in enumerate(detTopRowMinors):
            if id % 2 != 0:
                determinant = determinant * -1
            value += matrix[0][id] * determinant
        
        return value

class Inverse(Determinant):
    def matrixInverse(self, matrix, determinant):
        minorMatrix = []
        for rowId, row in enumerate(matrix):
            for columnId in range(len(row)):
                minor = self.getMinor(matrix, (rowId, columnId))
                minorMatrix.append(minor)
        
        determinants = []
        for minor in minorMatrix:
            determinants.append(self.matrixDeterminant(minor))

        determinantMatrix = []
        for row in range(len(matrix)):
            columnList = []
            for column in range(len(matrix[row])):
                columnList.append(((-1) ** (row+column+2) * determinants[row*len(matrix[row]) + column]))
            determinantMatrix.append(columnList)
        
        transposeMatrix = list(zip(*determinantMatrix))
        transposeMatrix = [list(x) for x in transposeMatrix]

        inverseMatrix = []
        for rowId, row in enumerate(transposeMatrix):
            columnList = []
            for columnId, column in enumerate(row):
                columnList.append((transposeMatrix[rowId][columnId] / determinant))
            inverseMatrix.append(columnList)

        return inverseMatrix

class Calculator():
    def run(self):
        getMatrix = GetMatrix()
        matrix = getMatrix.get()

        findDeterminant = Determinant()
        matrixDeterminant = findDeterminant.matrixDeterminant(matrix)

        findInverse = Inverse()
        approxMatrixInverse = findInverse.matrixInverse(matrix, matrixDeterminant)

        print("\nThe approximate inverse Matrix is:")
        print("\n".join(["\t".join([str(cell) for cell in rows]) for rows in approxMatrixInverse]))

if __name__ == "__main__":
    calc = Calculator()
    calc.run()