// Created by Michael Nath

#include <iostream>
#include <vector>

using namespace std;

int birthdayCakeCandles(vector<int> arr) {
    //find the largest element
    int tallest = arr[0];
    for (int x : arr) {
        if (x > tallest) tallest = x;
    }
    // search the vector for the occurences of that largest element
    int count = 0;
    for (int x : arr) {
        if (x == tallest) count++;
    }
    return count;
}

int main() {
    vector<int> arr(5);
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }
    cout << birthdayCakeCandles(arr) << endl;
    return 0;
}