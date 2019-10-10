public class CountDown {
	public static void main(String[] args) {
		int a = Integer.parseInt(args[0]);
		int counter = a;
		while (counter != 0) {
			System.out.println(counter);
			counter -= 1;
		}

		System.out.println("BLASTOFF");

	
	}
}