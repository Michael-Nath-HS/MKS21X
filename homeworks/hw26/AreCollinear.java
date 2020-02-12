public class AreCollinear {
	public static boolean areCollinear(int x1, int y1, int x2, int y2, int x3, int y3) {
		if (x1 == x2 && x2 == x3) return true;
		if ((1.0 * (y2 - y1) / (x2 - x1))  == ((1.0 * (y3 - y2) / (x3 - x2) ))) {
			return true;
		}
		return false;
	}

	public static boolean areCollinear(int x1, int y1, int x2, int y2, int ... args) {
		double slope = (1.0 * y2 - y1) / (x2 - x1);
		boolean checker = true;
		int curx = x1;
		int cury = y1;
		for (int i = 0; i < args.length; i += 2) {
			if (((double)(args[i + 1] - cury) / (args[i] - curx)) != slope) {
				checker = false;
			}
			curx = args[i];
			cury = args[i+1];
		}
		return checker;

}


	public static void main(String[] args) {
        System.out.println(areCollinear(8,6,2,6,5,8, 1,2,5,3));
		System.out.println(areCollinear(8,6,2,6,5,6,1,6));
		System.out.println(areCollinear(6,6,2,6,9,6));
	}
}