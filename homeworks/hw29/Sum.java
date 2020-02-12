package hw29;

public class Sum {
    public static int sum1(int n){
        return (n * (n + 1) / 2);
    }

    public static int sum2(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            ans += i;
        }
        return ans;
    }

    public static int sum3(int n) {
        if (n == 1) return 1;
        return n + sum3(n - 1);
    }

    public static int sum4(int n, int result) {
        if (n == 0) return result;
        return sum4(n - 1, n + result);
    }

    public static void main(String[] args) {
        System.out.println(sum1(100));
        System.out.println(sum2(100));
        System.out.println(sum3(100));
        System.out.println(sum4(100, 0));
    }

}
