// Gives the natural log of n!.

public class RecursiveLnFact {
    public static double Recurse(int a) {
        if (a == 1) return 0;
        return Math.log(a) + Recurse(a - 1);
        // 5 + 4 + 3 + 2 + 1
    }
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        double answer = Recurse(a);
        System.out.println(answer);
    }
}