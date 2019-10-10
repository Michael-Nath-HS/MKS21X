public class Median5 {
	public static void main(String[] args) {
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		int c = Integer.parseInt(args[2]);
		int d = Integer.parseInt(args[3]);
		int e = Integer.parseInt(args[4]);

		int max, min, res;
		int max = Math.max(Math.max(Math.max(a,b), Math.max(b, c)), 
			Math.max(Math.max(c,d), Math.max(d,e)))

		int sec_max = Math.min(Math.min(Math.min(a,b), Math.min(b, c)), 
			Math.max(Math.min(c,d), Math.min(d,e)));
		int res = a + b + c + d + e;
		res = res - (max + min)


}