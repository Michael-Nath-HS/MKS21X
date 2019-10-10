public class Trig {
//    Write a program Trig.java to illustrate various trigonometric functions in
//   the Math library, such as Math.sin(), Math.cos(), and Math.toRadians().
//   Your program should take a value in degrees and will need to convert
//   the degrees to radians in order to use Java's trigonometric functions.

    public static void main(String[] args) {
        double angle = Math.toRadians(Double.parseDouble(args[0]));
        double sine = Math.sin(angle);
        double cosine = Math.cos(angle);
        double tan = (sine / cosine);
        System.out.println("sine : " + sine);
        System.out.println("cosine : " + cosine);
        System.out.println("tangent : " + tan);
    }
}
