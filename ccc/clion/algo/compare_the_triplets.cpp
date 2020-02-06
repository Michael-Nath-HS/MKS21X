//
// Created by Michael Nath on 1/28/20.
//

#include <iostream>
#include <vector>

using namespace std;

vector<int> compareTriplets(vector<int> a, vector<int> b) {
    vector<int> ans;
    ans.push_back(0);
    ans.push_back(0);
    for (int i = 0; i < a.size(); i++) {
        if (a[i] < b[i]) {
            ans[1]++;
        }
        else if (a[i] > b[i]) {
            ans[0]++;
        }
    }
    return ans;
}

int main() {
    vector<int> a;
    vector<int> b;
    a.push_back(5);
    a.push_back(6);
    a.push_back(7);
    b.push_back(3);
    b.push_back(6);
    b.push_back(10);

    vector<int> res = compareTriplets(a, b);
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
