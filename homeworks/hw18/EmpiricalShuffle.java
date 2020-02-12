public class EmpiricalShuffle {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int n = Integer.parseInt(args[1]);
        int[][] table = new int[m][m];
        for (int z = 0; z < n; z++) {
            int[] deck = new int[m];
            for (int i = 0; i < m; i++) {
                deck[i] = i;
            }
            for (int k = 0; k < m; k++) {
                int r = k + (int) (Math.random() * (m - k));
                int temp = deck[r];
                deck[r] = deck[k];
                deck[k] = temp;
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < m; j++) {
                    if (i == deck[j]) {
                        table[i][j]++;
                    }
                }
            }

            }
        for (int j = 0; j < table.length; j++) {
            for (int k = 0; k < table[0].length; k++) {
                System.out.print(table[j][k] + "\t");
            }
            System.out.println();
        }
    }
}
