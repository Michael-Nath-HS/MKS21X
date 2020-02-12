public class BrownianBridge {
    public static void toDraw(double x0, double y0, double x1, double y1, double variance, double sFactor) {
        // does stuff
        if (Math.abs(x0 - x1) < 0.01) StdDraw.line(x0, y0, x1,y1);
        else {
            double xm = (x0 + x1) / 2;
            double ym = (y0 + y1) / 2;
            double delta = StdRandom.gaussian(0.0, Math.sqrt(variance));
            ym += delta;
            toDraw(x0, y0, xm, ym, variance / sFactor, sFactor);
            toDraw(xm, ym, x1, y1, variance / sFactor, sFactor);
        }
    }
    
    public static void main(String[] args) {
        double hurst = Double.parseDouble(args[0]);
        StdDraw.setScale(-1.5, 1.5);
        double sFactor = Math.pow(2, 2 * hurst);
        toDraw(0, 0.5, 1, 0.5, 0.01, sFactor);
    }
}
