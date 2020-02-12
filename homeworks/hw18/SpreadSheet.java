public class SpreadSheet{

    public static void main(String [] args) {
		// a is a 11 x 4
		// a represents a spreadsheet containing
		// the 3 test scores for 10 students.
		double[][] a = {
				{99.0, 85.0, 98.0, 0.0},
				{98.0, 57.0, 79.0, 0.0},
				{92.0, 77.0, 74.0, 0.0},
				{94.0, 62.0, 81.0, 0.0},
				{99.0, 94.0, 92.0, 0.0},
				{80.0, 76.5, 67.0, 0.0},
				{76.0, 58.5, 90.5, 0.0},
				{92.0, 66.0, 91.0, 0.0},
				{97.0, 70.5, 66.5, 0.0},
				{89.0, 89.5, 81.0, 0.0},
				{0.0, 0.0, 0.0, 0.0}
		};

		double bank1 = 0.0;
		double bank2 = 0.0;
		double bank3 = 0.0;
		double bank4 = 0.0;
		double[] weights = {0.25, 0.25, 0.50};

		for (int i = 0; i < a.length - 1; i++) {
			a[i][3] = ((weights[0] * a[i][0]) + (weights[1] * a[i][1]) + (weights[2] * a[i][2]));
			bank1 += (a[i][0]) ;
			bank2 += a[i][1];
			bank3 += a[i][2];
			bank4 += a[i][3];
		}

		for (int i = 0; i < a[0].length; i++) {
			a[a.length - 1][0] = (bank1 / a.length);
			a[a.length - 1][1] = (bank2 / a.length);
			a[a.length - 1][2] = (bank3 / a.length);
			a[a.length - 1][3] = (bank4 / a.length);
		}

		for (int j = 0; j < a.length; j++) {
			for (int k = 0; k < a[0].length; k++) {
				System.out.print(a[j][k] + "\t");
			}
			System.out.println();
		}
	}
}
