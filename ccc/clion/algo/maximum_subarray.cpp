#include <iostream>
#include <vector>

using namespace std;
typedef vector<int> intA;
typedef long long ll;

int maxSumOne(intA &arr) {
    // O(n^3) solution
    int sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i; j < arr.size(); j++) {
            int testSum = 0;
            for (int k = i; k <= j; k++) {
                testSum += arr[k];
            }
            sum = max(testSum, sum);
        }
    }
    return sum;
}

int maxSumTwo(intA &arr) {
    // O(n^2) solution
    int sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        int testSum = 0;
        for (int j = i; j < arr.size(); j++) {
            testSum += arr[j];
            sum = max(testSum, sum);
        }
    }
    return sum;
}

int maxSumThree(intA &arr) {
    int best, sum = 0;
    for (int k = 0; k < arr.size(); k++) {
        sum = max(arr[k], sum + arr[k]);
        best = max(best, sum);
    }
    return best;
}

int main() {
    int n; 
    cin >> n;
    intA test;
    for (int i = 0; i < n; i++) {
        int elem;
        cin >> elem;
        test.push_back(elem);
    }
    cout << maxSumOne(test) << "\n";
    cout << maxSumTwo(test) << "\n";
    cout << maxSumThree(test) << "\n";

}