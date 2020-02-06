//
// Created by Michael Nath on 1/26/20.
//
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int size;
    cin >> size;
    int sum = 0;
    for (int i = 0; i < size; i++) {
        int n;
        cin >> n;
        sum += n;
    }
    cout << sum << endl;
    return 0;
}