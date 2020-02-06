#include <iostream>
#include <vector>

using namespace std;

vector<int> insert(vector<int> arr, int val, int index) {
    vector<int> ans(arr.size() + 1);
    for (int i = 0; i < ans.size(); i++) {
        if (i < index) ans[i] = arr[i];
        else if (i == index) ans[index] = val;
        else ans[i] = arr[i - 1];
    }

    return ans;
}

vector<int> climbingLeaderboard(vector<int> scores, vector<int> alice) {
    for (int x : alice) {
        int index = -1;
        if (x > scores[0]) {
            scores = insert(scores, x, 0);
            index = 1;
        }
        else if (x < scores[scores.size() - 1]) {
            scores = insert(scores,x,scores.size());
            index = scores.size();
        }
        else {
            for (int i = 0; i < scores.size() - 1; i++) {
                if (scores[i] >= x && scores[i + 1] < x) {
                    index = i + 1;
                }
            }
            scores = insert(scores, x, index);
            index += 1;
        }
        int count = 1;
        for (int i = 0; i < scores.size(); i++) {
            if (scores[i] == x) break;
            if (i == scores.size() - 1) break;
            if (scores[i] != scores[i + 1]) count++;
        }
        cout << count << endl;
    }
    return scores;
}

int main() {
    vector<int> scores;
    vector<int> alice;
    scores.push_back(100);
    scores.push_back(100);
    scores.push_back(50);
    scores.push_back(40);
    scores.push_back(40);
    scores.push_back(20);
    scores.push_back(10);
    alice.push_back(5);
    alice.push_back(25);
    alice.push_back(50);
    alice.push_back(120);
    vector<int> inserted = climbingLeaderboard(scores, alice);

    // for (int x : inserted) {
    //     cout << x << "\t";
    // }
    // cout << endl;
}