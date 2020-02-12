#include <iostream>
#include <cmath>
using namespace std;

int reverse(int x) {
    int num = fabs(x);
    if (num > INT_MAX || num < INT_MIN) return 0;
    int length = 0;
    int temp = num;
    while (temp > 0) {
        temp /= 10;
        length++;
    }
    int ans = 0;
    int ten = 0;
    while (num > 0) {
        int temp = (num % 10);
        ans += (temp * (int) (pow(10, length - ten - 1)));
        ten++;
        num /= 10;
    }
    ans = (x < 0) ? -1 * ans : ans;
    return ans;
}

int main() {
    cout << reverse(-182) << endl;
    return 0;
}