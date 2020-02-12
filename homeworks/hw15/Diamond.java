public class Diamond {
    public static void main(String[] args) {
        int org = Integer.parseInt(args[0]);
        int n = (2 * Integer.parseInt(args[0])) + 1;
        for (int i = 0; i < n / 2 ; i++) {
            for (int j = 0; j < n ; j++) {
                if (j >= (org - (i % org)) && j <= (org + (i % org ))) {
                    System.out.print("* ");
                }
                else System.out.print(". ");
            }
            System.out.println();
        }

        for (int k = (n / 2) + 1; k <= n; k++) {
            for (int l = 0; l < n; l++) {
                if (l >= org - (n % k) && l <= org + (n % k)) System.out.print("* ");
                else System.out.print(". ");
            }
            System.out.println();
        }
    }
}
