//
// Created by Michael Nath on 12/24/19.
//

#include <iostream>
using namespace std;


int main() {
    cout << "Give me two numbers and I will tell you all the "
            "odd numbers in the range" << endl;
    int n1, n2 = 0;
    cin >> n1 >> n2;
    for (int i = n1; i <= n2; i++) {
        if (i % 2 != 0) cout << i << "\t";
    }
    return 0;
}