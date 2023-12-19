import java.util.Scanner;
// import java.util.Arrays; // For printing matrices

public class calculator {
    public static void main(String[] args) {
        float[][] matrix = GetMatrix.get();

        float findDeterminant = Determinant.getDeterminant(matrix);
        System.out.println(String.format("The determinant is %f", findDeterminant));
    }
}

class GetMatrix {
    public GetMatrix() {}
    
        public static float[][] get() { // float[][]
            message();
    
            String correct = "";
            float[][] matrix = {};
    
            Scanner matrixScanner = new Scanner(System.in);
            while (correct != "y") {
                System.out.println(":");
                String stringMatrix = matrixScanner.nextLine();

                matrix = sanitise(stringMatrix);
                if (matrix.length >= 1) {
                    correct = "y";
                }
            }
            matrixScanner.close();

            return matrix;
        }

    public static void message() {
        System.out.println("""
            Welcome to the determinant calculator
            You can only calculate the determinant of square matrix
            Enter your matrix like this:
            [1 2] --> 1,2,3,4 or 1, 2, 3, 4
            [3 4]

            [1 2 3]
            [4 5 6] --> 1,2,3,4,5,6,7,8,9 or 1, 2, 3, 4, 5, 6, 7, 8, 9
            [7 8 9]

            etc.""");
    }

    public static float[][] sanitise(String matrixString) {
        float[][] returnBad = {};

        matrixString = matrixString.replace(" ", "");
        String[] halfMatrix = matrixString.split(",");

        if (Math.sqrt(halfMatrix.length) % 1 != 0) { 
            String errorMessage = """
                You have entered %d numbers
                A determinant can only be found for square matices
                This means that the number of elements in your matrix but be a square number
                Please re-enter your matrix""";
            System.out.println(String.format(errorMessage, halfMatrix.length));
            return returnBad;
        }
        int size = (int)Math.sqrt(halfMatrix.length);

        if (size >= 10) {
            String warningMessage = """
                    Matrices over 10x10 have been found to take 2 minutes or more during testing
                    Enter 'stop' to cancel this matrix calculation and enter another""";
            System.out.println(warningMessage);
            Scanner warningScanner = new Scanner(System.in);
            System.out.println(":");
            String answer = warningScanner.nextLine();
            warningScanner.close();

            if (answer.toLowerCase() == "stop") {
                return returnBad;
            }
        }

        float[][] matrix = new float[size][size];
        float value;
        int counter = 0;
        for (int i = 0; i < halfMatrix.length; i += size) {
            float[] columnArray = new float[size];
            for (int j = 0; j < size; j++) {
                try {
                    value = Float.parseFloat(halfMatrix[i+j]);
                    columnArray[j] = value;
                }
                catch (NumberFormatException e) {
                    System.out.println(e);
                }
            }
            matrix[counter] = columnArray;
            counter++;
        }

        return matrix;
    }
}

class Minor {
    public static float[][] getMinor(float[][] matrix, int[] pos) {
        int rowIgnore = pos[0];
        int columnIgnore = pos[1];

        float[][] minor = new float[matrix.length-1][matrix.length-1];

        int rowModifier = 0;
        int columnModifier = 0;
        for (int row = 0; row < matrix.length; row++) {
            if (row == rowIgnore) {
                rowModifier = -1;
                continue;
            }

            float[] columnArray = new float[matrix.length-1];
        
            columnModifier = 0;
            for (int column = 0; column < (matrix[row].length); column++) {
                if (column == columnIgnore) {
                    columnModifier = -1;
                    continue;
                }

                columnArray[column+columnModifier] = matrix[row][column];
            }

            minor[row+rowModifier] = columnArray;
        }
    
        return minor;
    }
}

class Determinant {
    public static float getDeterminant(float[][] matrix) {
        float[] detTopRowMinors = new float[matrix.length];

        if (matrix.length == 1) {
            return matrix[0][0];
        }

        if (matrix.length == 2) {
            float ad = matrix[0][0] * matrix[1][1];
            float bc = matrix[1][0] * matrix[0][1];
            return ad-bc;
        }

        for (int id = 0; id < (matrix[0].length); id++) {
            int[] pos = {0, id};
            float[][] minor = Minor.getMinor(matrix, pos);

            float detMinor = getDeterminant(minor);

            detTopRowMinors[id] = detMinor;
        }

        float value = 0;
        for (int id = 0; id < detTopRowMinors.length; id++) {
            float determinant = detTopRowMinors[id];
            if (id % 2 != 0) {
                determinant = determinant * -1;
            }
            value += matrix[0][id] * determinant;
        }
        
        return value;
    }
}