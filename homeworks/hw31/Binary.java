public class Binary {
    /* Write a program that takes a positive integer n (as a decimal)
   as a command-line argument and converts n to its binary representation
   with the following three methods.

   Each method uses the following algorithm to convert from decimal to
   binary:  repeatedly divide 2 into n and read the remainders backward. */

//    First, write a while loop to carry out this computation and print the bits in the wrong order.
    public static void printBinary(int n) {
//        Algo: Take number, integer divide by 2, save the remainder. Repeat
        String ans = "";
        while (n != 0) {
//          converts the remainder to string and adds that to ans string
            ans += Integer.toString(n % 2);
//          updates iteration
            n /= 2;
        }
//      print out the answer
        System.out.println(ans);
    }


//    Second, use recursion to print the bits in the correct order.
    public static void printBinaryR(int n) {
        // first base case: if n mod 2 is 1, print 1. else, print 0
        if (n > 0) {
            printBinaryR(n / 2);
            System.out.print(n % 2);
        }
    }

    public static String toBinary(int n) {
        if (n == 0) return "";
        return toBinary(n / 2) + (n % 2);

    }

    public static void main(String[] args) {
        printBinary(51231); // Should output 010011
        printBinaryR(51231); // Should output 110010
        System.out.println();
        System.out.println(toBinary(51231)); // Should output 110010
    }

}
