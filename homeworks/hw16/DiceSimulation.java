public class DiceSimulation {
    public static void main(String[] args) {
        int [] megafreq = new int[13];
        int n = Integer.parseInt(args[0]);
        double[] probabilities = new double[13];
        for (int county = 0; county < n; county++) {
            int [] frequencies = new int[13];
            for (int i = 1; i <= 6; i++)
                for (int j = 1; j <= 6; j++)
                    frequencies[i + j]++;

            for (int k = 1; k <= 12; k++) {
                probabilities[k] = frequencies[k] / 36.0;
            }
            for (int z = 1; z <= 12; z++) {
                megafreq[z] += frequencies[z];
            }
        }

        for (int k = 1; k <= 12; k++) {
            System.out.println("Probablity of " + k + ": " + probabilities[k]);
        }
        for (int counter = 1; counter <= 12; counter++) {
            System.out.println("Empirical Probability: " + megafreq[counter] / (36.0 * n));
        }
    }
}
