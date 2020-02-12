/*
  In the program StringReverse.java implement the methods:

   a. Write a static method reverse() that takes an array of strings
      as its argument and returns a new array with the strings in
      reverse order. (Do Not PRODUCE ANY SIDE EFFECTS).


   b. Write a static method reverseInPlace() that takes an array of
      strings as its argument and produces the side effect of reversing
      the order of the strings in the argument array.

  Here's a sample run:

  $java StringReverse a b c d
   args before reverse:
   a b c d 
   reverse(args): 
   d c b a 
   args after reverse: 
   a b c d 
   args after reverseInPlace:
   d c b a 
*/

public class StringReverse {

    // swap elements at index i and j via a side effect
    public static void swap(String[] a, int i, int j) {
        String temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static void print(String[] a) {
        for (String x : a)
            System.out.print(x + " ");
        System.out.println();
    }


    public static String[] reverse(String[] a) {
        // YOUR CODE GOES HERE
        // given an array of Strings, return a new array with the strings going in reverse order
        // create an answer array that will be returned
        String[] ans = new String[a.length];
        int iter = 0;
        for (int i = a.length - 1; i >= 0; i--) {
            ans[i] = a[iter];
            iter++;
//            s.length = 5; 4 --> 3 --> 2 --> 1 --> 0
//                          0 --> 1 --> 2 --> 3 --> 4
        }
        return ans;
    }

    public static void reverseInPlace(String[] args) {
        for (int i = 0; i < args.length / 2; i++) {
            swap(args, i, args.length - i - 1);
//            s.length = 5; 4 --> 3 --> 2 --> 1 --> 0
//                          0 --> 1 --> 2 --> 3 --> 4
        }
//

    }

    public static void main(String[] args) {
        System.out.println("args before reverse:");
        print(args);
        System.out.println("reverse(args): ");
        print(reverse(args));
        System.out.println("args after reverse(args): ");
        print(args);
	    reverseInPlace(args);
	    System.out.println("args after reverseInPlace(args):");
	    print(args);

    }

}
