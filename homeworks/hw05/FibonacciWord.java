
/* Write a program FibonacciWord.java
    that prints the Fibonacci word of order 0 through 10.
    f(0) = "a", f(1) = "b", f(2) = "ba", f(3) = "bab", f(4) = "babba",
    and in general f(n) = f(n-1) followed by f(n-2).
    Use string concatenation.
    */
public class FibonacciWord {
    // Recursive Method just for fun
    public static String Fibbonaci(int n) {
        if (n == 0) {
            return "a";
        } else if (n == 1) {
            return "b";
        } else {
            return Fibbonaci(n - 1) + Fibbonaci(n - 2);
        }
    }

    public static void main(String[] args) {
        String fib0 = "a";
        String fib1 = "b";
        String fib2 = fib1 + fib0;
        String fib3 = fib2 + fib1;
        String fib4 = fib3 + fib2;
        String fib5 = fib4 + fib3;
        String fib6 = fib5 + fib4;
        String fib7 = fib6 + fib5;
        String fib8 = fib7 + fib6;
        String fib9 = fib8 + fib7;
        String fib10 = fib9 + fib8;

        System.out.println(fib0);
        System.out.println(fib1);
        System.out.println(fib2);
        System.out.println(fib3);
        System.out.println(fib4);
        System.out.println(fib5);
        System.out.println(fib6);
        System.out.println(fib7);
        System.out.println(fib8);
        System.out.println(fib9);
        System.out.println(fib10);
        System.out.println(Fibbonaci(4));
        System.out.println(Fibbonaci(10));
    }

}

