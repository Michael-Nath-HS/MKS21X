import java.util.Arrays;

public class SelectionSort {
    public static int[] sort(int[] a) {
        if (a.length <= 1) return a;
        for (int i = 0; i < a.length; i++) {
            int low = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[low]) low = j;
            }
            int temp = a[i];
            a[i] = a[low];
            a[low] = temp;
        }
        return a;
    }
    public static void main(String[] args) {
        int[] array = {7, 2 ,5, 1, 8, 3};
        System.out.println(Arrays.toString(sort(array)));
    }
}
