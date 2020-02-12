public class MissingInt {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        boolean[] vals = new boolean[n+1];
        for (int i = 0; i < n - 1; i++) {
            int a = StdIn.readInt();
            if (a < 1 || a > n || vals[a]) {
                System.out.println("Submit Again");
                i--;
            }
            else {
                vals[a] = true;
            }
        }
        for (int i = 1; i < vals.length; i++) {
            if (!vals[i]) System.out.println("Missing Value is " + i);
        }
    }
}
