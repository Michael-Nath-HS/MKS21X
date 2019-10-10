public class GreatCircle {
	public static void main(String[] args) {
		// d = 60arccos(sin(x1)sin(x2) + cos(x1)cos(x2)cos(y1-y2))
		// The inputs are given in degrees, so we need to convert them into radians
		double x1 = Math.toRadians(Double.parseDouble(args[0]));
		double y1 = Math.toRadians(Double.parseDouble(args[1]));
		double x2 = Math.toRadians(Double.parseDouble(args[2]));
		double y2 = Math.toRadians(Double.parseDouble(args[3]));

		// Sub into the equation, knowing that each trig function will take in radians. 
		double d = 60 * (Math.toDegrees(Math.acos((Math.sin(x1) * Math.sin(x2)) + (Math.cos(x1) * Math.cos(x2) * Math.cos(y1 - y2)))));
		System.out.println("Miles: " + d);

	}
}