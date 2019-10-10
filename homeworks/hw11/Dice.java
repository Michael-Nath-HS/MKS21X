public class Dice {
    public static void main(String[] args) {
        int range = 6;
        int a = (int)((Math.random() * range) + 1);
        int b = (int)((Math.random() * range) + 1);
        System.out.println(a + b);
    }
}
