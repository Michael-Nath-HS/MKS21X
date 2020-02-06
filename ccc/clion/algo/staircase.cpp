// Created by Michael Nath



#include <iostream>
#include <string>
using namespace std;


void staircase(int n) {
    for (int i = 0; i < n; i++) {
        string str;
        for (int j = 0; j < n - i; j++) {
            str += " ";
        }
        for (int j = n - i - 1; j < n; j++) {
            str += "#";
        }
        cout << str << endl;
    }
}

int main() {
    staircase(4);
    return 0;
}