public class ReverseTwentyQuestions {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        boolean [] nums = new boolean[b + 1];
        for (int i = 1; i <= b; i++) {
            if (i >= a) nums[i] = true;
        }

        int iter = nums.length / 2;
        boolean check = false;
        while (!check) {
            System.out.println("Is the number %d <true,false>? :" + nums[iter]);
            if (StdIn.readBoolean()) check = true;
            else {
                System.out.println("Am I too low? <true,false> :");
                if (StdIn.readBoolean()) {

                }
            }
        }

    }
}
