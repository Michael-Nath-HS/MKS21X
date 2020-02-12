#include <iostream>
#include <vector>

using namespace std;


void swap(vector<int> &arr, int i1, int i2) {
    int temp = arr[i1];
    arr[i1] = arr[i2];
    arr[i2] = temp;
}

void bubbleSort(vector<int> &arr) {
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr.size() - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
            }
        }
    }
 }

 int main() {
     vector<int> arr;
     int n;
     cin >> n;
     int x;
     while (cin >> x) {
         arr.push_back(x);
     }
     bubbleSort(arr);
     for (int i : arr) {
         cout << i << " ";
     }
     cout << endl;
     return 0;
 }