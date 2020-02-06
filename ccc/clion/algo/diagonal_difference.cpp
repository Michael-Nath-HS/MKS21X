//
// Created by Michael Nath on 1/29/20.
//

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int diagonalDifference(vector<vector<int> > arr) {
    int lr_sum = 0;
    int menter = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[0].size(); j++) {
            if (j == menter) lr_sum += arr[i][j];
        }
        menter++;
    }
    int rl_sum = 0;
    menter = arr[0].size() - 1;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[0].size(); j++) {
            if (j == menter) rl_sum += arr[i][j];
        }
        menter--;
    }
    return fabs(rl_sum - lr_sum);
}

int main() {
    vector<vector<int> > arr(
            3,
            vector<int>(3)
    );
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[0].size(); j++) {
            arr[i][j] = (2*i) + j;
        }
    }
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[0].size(); j++) {
            cout << arr[i][j] << "\t";
        }
        cout << endl;
    }
    cout << diagonalDifference(arr) << endl;
    return 0;
}