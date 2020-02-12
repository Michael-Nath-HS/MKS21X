public class Minesweeper {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int n = Integer.parseInt(args[1]);
        double p = Double.parseDouble(args[2]);
        int [][] nbombs = new int[m+2][n+2];

        boolean [][] field = new boolean[m+2][n+2];
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1 ; j < n + 1; j++){
                if (Math.random() < p) field[i][j] = true;
                else field[i][j] = false;
            }
        }

        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (!field[i][j]) {
                    boolean [] neighbors = {
                            field[i - 1][j],
                            field[i + 1][j],
                            field[i][j + 1],
                            field[i][j-1],
                            field[i-1][j - 1],
                            field[i - 1][j + 1],
                            field[i + 1][j - 1],
                            field[i + 1][j + 1]
                    };
                    for (int iter = 0; iter < neighbors.length; iter++) {
                        if (neighbors[iter]) nbombs[i][j]++;
                    }
                }
            }
        }

        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++){
                String smth = (field[i][j]) ? "*" :  ".";
                System.out.print(smth + "\t");
            }
            System.out.println();

        }
        System.out.println();
        System.out.println();
        System.out.println();
        System.out.println();

        for (int i = 1; i < m + 1; i++) {
            for (int j = 1 ; j < n + 1; j++){
                if (field[i][j]) System.out.print("*" + "\t");
                else System.out.print(nbombs[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
