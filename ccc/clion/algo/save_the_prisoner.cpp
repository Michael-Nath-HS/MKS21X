#include <iostream>
#include <vector>

using namespace std;

int saveThePrisoner(int n, int m, int s) {
    int ans = (s + m - 1) % n;
    if (ans == 0) return n;
    return ans;
}

int main() {
    cout << saveThePrisoner(7, 19, 2) << endl;

    return 0;
}