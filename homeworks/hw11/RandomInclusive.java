public class RandomInclusive {
    public static void main(String[] args) {
        int a,b;
        a = Integer.parseInt(args[0]);
        b = Integer.parseInt(args[1]);
        double c = Math.random();
        double d = c * (Math.max(a,b) - Math.min(a,b) + 1);
        d = d + Math.min(a,b);
        System.out.println((int) d);
    }
}
