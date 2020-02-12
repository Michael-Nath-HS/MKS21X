public class Hadamard {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]); // n command line
        boolean[][] matrix = new boolean[n][n];
        matrix[0][0] = true;
//        boolean[][] prev = new boolean[n][n];
        boolean[][] prev = {{true}};
        int m = 2;
        if (n > 1) {
            for (int trials = 0; trials < n / 2; trials++) {
                int start = m / 2;
                int stop = m - 1;
                for (int iter = 0; iter < m; iter++) {
                    for (int j = 0; j < m; j++) {
                        if (!((j >= start && j <= stop) && (iter >= start && iter <= stop))) {
                            matrix[iter][j] = prev[iter % m][iter % m];
                        } else {
                            matrix[iter][j] = !prev[iter % m][iter % m];
                        }
                    }
                }
                prev = matrix;
                m*= 2;
//                matrix = new boolean[m][m];
            }
        }

        for (int z = 0; z < n; z++) {
            for (int y = 0; y < n; y++) {
                System.out.print(matrix[z][y] + "\t");
            }
            System.out.println();
        }
    }

}
