#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getTotalX(vector<int> a, vector<int> b) {
    int maxA = *max_element(a.begin(), a.end());
    int minB = *min_element(b.begin(), b.end());
    vector<int> pos;
    int count = 0;
    // cout << maxA << " " << minB << endl;
    for (int i = maxA; i <= minB; i++) {
        bool gate = true;
        for (int x : a) {
            if (i % x != 0) gate = false;
        }
        if (gate) {
            // cout << i << endl;
            pos.push_back(i);
        }
    } 
    
    for (int j : pos) {
        bool gate = true;
        for (int k : b) {
            if (k % j != 0) gate = false;
        }
        if (gate) count++;
    }
    return count;
}

int main() {
    vector<int> a;
    vector<int> b;
    a.push_back(2);
    a.push_back(4);
    b.push_back(16);
    b.push_back(32);
    b.push_back(96);
    
    cout << getTotalX(a,b) << endl;
}
