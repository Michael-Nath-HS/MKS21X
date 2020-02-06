// Created by Michael Nath



#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

/*
A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
*/

void plusMinus(vector<int> arr) {
    vector<double> zero(1); vector<double> pos(1); vector<double>neg(1);
    for (int x : arr) {
        if (x > 0) pos[0]++;
        else if (x < 0) neg[0]++;
        else zero[0]++;
    }
    cout << fixed << setprecision(6) << pos[0] / arr.size() << endl;
    cout << fixed << setprecision(6) << neg[0] / arr.size() << endl;
    cout << fixed << setprecision(6) << zero[0] / arr.size() << endl;
}

int main() {
    vector<int> arr;
    arr.push_back(-4);
    arr.push_back(3);
    arr.push_back(-9);
    arr.push_back(0);
    arr.push_back(4);
    arr.push_back(1);
    for (int i : arr) {
        cout << i << " ";
    }
    cout << endl;
    plusMinus(arr);
    return 0;
}