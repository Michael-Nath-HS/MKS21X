package hw29;

public class EuclidAlgo {
    public static long gcd(long a, long b) {
        if (a % b == 0) return b;
        return gcd(b, a % b);
    }
    public static void main(String[] args) {

        long a = 82312536;
        for (long i = 1; i <= a; i++){
            if (gcd(a,i) == i) System.out.println(i + " is factor");;
        }


    }
}
