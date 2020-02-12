public class MethodTest {
	public static int f1() {
		System.out.println("f1");
		return 1;
	}
	public static int f2() {
		System.out.println("f2");
		return 2;
	}


	public static int f3(int x, int y) {
		System.out.println("f3");
		return x * y;
	}

	public static int f4() {
		System.out.println("f4");
		return 5;
	}

	public static int f5() {
		System.out.println("f5");
		return 6;
	}
	public static void main(String[] args) {
		System.out.println(f1() + f2() * f3(f4(), f5()));
	}
}