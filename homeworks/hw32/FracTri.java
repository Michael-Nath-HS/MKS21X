public class FracTri {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        double[][] tri = {
                {0, 0},
                {0.5, (Math.sqrt(3) / 4)},
                {1, 0}
        };
        StdDraw.setYscale(0, (Math.sqrt(3) / 4));
        int rPicker = (int) (Math.random() * 3);
        double initX = tri[rPicker][0];
        double initY = tri[rPicker][1];
        StdDraw.point(initX, initY);
        for (int i = 1; i < n; i++) {
            int iterPicker = (int) (Math.random() * 3);
            StdDraw.point(
                    ((initX + tri[iterPicker][0]) / 2),
                    ((initY + tri[iterPicker][1]) / 2)
            );
            initX = (initX + tri[iterPicker][0]) / 2;
            initY = (initY + tri[iterPicker][1]) / 2;
        }
    }
}
