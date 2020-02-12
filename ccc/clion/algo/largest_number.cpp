#include <iostream>
#include <vector>

using namespace std;

int main() {
    int s;
    cin >> s;
    vector<int> arr;
    for (int i = 0; i < s; i++) {
        int x;
        cin >> x;
        arr.push_back(x);
    }
    cout << arr[0] << "\n";
    sort(arr.begin(), arr.end());
    cout << arr[0] << endl;

}