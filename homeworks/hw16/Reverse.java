public class Reverse {
    public static void main(String[] args) {
        String [] rev = new String[args.length];
        for (int i = 0; i < args.length; i++) {
            rev[i] = args[i];
        }
        String k = rev[args.length - 1];
        for (int j = 0; j < (args.length / 2); j++) {
            k = rev[args.length - j - 1];
            String z = rev[j];
            rev[j] = k;
            rev[args.length - j - 1] = z;
//           [0, 1, 2, 3] --> [3, 2, 1, 0]
        }
        for (int l = 0; l < args.length; l++){
            System.out.println(rev[l]);
        }
    }
}
