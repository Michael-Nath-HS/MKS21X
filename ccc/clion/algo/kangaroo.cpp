#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

string Kangaroo(int x1, int v1, int x2, int v2) {
    if (x1 == x2) return "YES";
    if ((x2 > x1 && v2 >= v1) || (x1 > x2 && v1 >= v2)) return "NO";
    double res = fabs(x2 - x1);
    double lOver = fabs(v2 - v1);
    if (ceil(res / lOver) == (res/lOver)) {
        return "YES";
    }
    return "NO";
}

int main() {
    cout << Kangaroo(0, 3, 4, 2) << endl;
    cout << Kangaroo(0, 2, 5, 3) << endl;
    cout << Kangaroo(21, 6, 47, 3) << endl;


    return 0;
}