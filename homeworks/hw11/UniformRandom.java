public class UniformRandom {
    public static void main(String[] args) {
        double a,b,c,d,e;
        a = Math.random();
        b = Math.random();
        c = Math.random();
        d = Math.random();
        e = Math.random();
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(.2 * (a + b + c + d + e));
        double min = Math.min(a,b);
        min = Math.min(min, c);
        min = Math.min(min, d);
        min = Math.min(min, e);
        double max = Math.max(a,b);
        max = Math.max(max, c);
        max = Math.max(max, d);
        max = Math.max(max, e);
        System.out.println(min);
        System.out.println(max);
        System.out.println((int)(Math.random()));



    }
}
