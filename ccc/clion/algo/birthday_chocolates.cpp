#include <iostream>
#include <vector>
#include <time.h>
using namespace std;


int birthday(vector<int> s, int d, int m) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        int sum = 0;
        for (int j = i; j < i + m; j++) {
            sum += s[j]; 
        }
        if (sum == d) count++;
    }
    return count;
} 

int main() {
    clock_t start, end;
    start = clock();
    int a;
    cin >> a;
    vector<int> s(a);
    for (int i = 0; i < a; i++) {
        int a;
        cin >> a;
        s[i] = a;
    }
    int d, m;
   dcin >> d >> m;
    cout << birthday(s, d, m) << endl;
    end = clock();
    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    cout << "\n" << endl;
    cout << cpu_time_used << endl;
    
    return 0;
}