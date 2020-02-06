import java.util.Scanner;
public class ArraySum {
//   Find the sum of Integer and Double arrays

    public static int intSum(int[] a) {
        int sum = 0;
        for (int i : a) {
            sum += i;
        }
        return sum;
    }

    public static double doubleSum(double[] a) {
        double sum = 0;
        for (double i : a) {
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int size = in.nextInt();
        System.out.println(size);
//        String[] a = in.nextLine();
    }
}
