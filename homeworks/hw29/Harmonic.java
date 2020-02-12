package hw29;

public class Harmonic {
    public static double harmonic(int n) {
        if (n == 1) return 1;
        return 1.0/n + harmonic(n - 1);
    }
    public static void main(String[] args) {
        System.out.println(harmonic(5));
    }
}
