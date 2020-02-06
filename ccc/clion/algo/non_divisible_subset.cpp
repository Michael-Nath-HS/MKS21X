#include <iostream>
#include <vector>

using namespace std;

vector<int> nonDivisibleSubset(int k, vector<int> s) {
    // brute force approach
    vector<int> test;
        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j < s.size(); j++) {
                if ((s[i] + s[j]) % k == 0) {
                    test.push_back(s[i]);
                    test.push_back(s[j]);
            }
        }
    }
    return test;
}

int main() {
    // while (cin >> )
    return 0;
}