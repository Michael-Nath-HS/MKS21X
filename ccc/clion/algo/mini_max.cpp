#include <iostream>
#include <vector> 
using namespace std;

int fact(int n ) {
    if (n == 1) return 1;
    return n * fact(n - 1);
}

void minMax(vector<int> arr) {
    long int sum = 0;
    for (int x : arr) {
        sum += x;
    }
    long int min_num = min(arr[0], min(arr[1], min(arr[2], min(arr[3], arr[4]))));
    long int max_num = max(arr[0], max(arr[1], max(arr[2], max(arr[3], arr[4]))));
    cout << sum - max_num << " " << sum - min_num << endl;
}

int main() {
    vector<int> arr(5);
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }
    minMax(arr);
    return 0;
}