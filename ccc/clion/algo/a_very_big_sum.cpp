//
// Created by Michael Nath on 1/28/20.
//

#include <iostream>
#include <vector>

using namespace std;

// const vector<long>& ar keeps the array static because it will not get changed. Saves memory ig
long aVeryBigSum(const vector<long>& ar) {
    long sum = 0;
    for (long i : ar) {
        sum += i;
    }
    return sum;
}

int main() {
    vector<long> inpt(5);
    for (int i = 0; i < inpt.size(); i++) {
        cin >> inpt[i];
    }
    cout << aVeryBigSum(inpt) << endl;
    return 0;
}