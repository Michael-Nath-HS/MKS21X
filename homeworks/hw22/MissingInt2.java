public class MissingInt2 {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int num1 = 0;
        int num2 = 0;
        for (int i = 0; i < n-1; i++) {
            num1 += StdIn.readInt();
        }

        for (int i = 1; i <= n; i++) {
            num2 += i;
        }

        System.out.println(num1 - num2);
    }
}
