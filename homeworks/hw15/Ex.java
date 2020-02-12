public class Ex {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (j <= i || j >= (n - i)) System.out.print("* ");
                else System.out.print(". ");
            }
            System.out.println();
        }
    }
}
