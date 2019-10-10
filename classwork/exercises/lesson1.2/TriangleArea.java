public class TriangleArea {
//    area = sqrt(s(s-a)(s-b)(s-c)), where s = (a + b + c) / 2.
public static void main(String[] args) {
    double a = Double.parseDouble(args[0]);
    double b = Double.parseDouble(args[1]);
    double c = Double.parseDouble(args[2]);
    double s = (a + b + c) / 2;
    double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
    System.out.println(area);
    }
}
