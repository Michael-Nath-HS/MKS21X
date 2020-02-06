//
// Created by Michael Nath on 12/24/19.
//

#include <iostream>
using namespace std;


int main() {
    int n1, n2;
    cout << "Give 2 Numbers" << endl;
    cin >> n1 >> n2;
    int sum = 0;
    for (int i = n1; i <= n2; i++) {
        sum += i;
    }
    cout << "The Sum is: " << sum << endl;

}