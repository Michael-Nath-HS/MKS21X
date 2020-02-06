#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> gradingStudents(vector<int> grades) {
    vector<int> newGrades;
    for (int i = 0; i < grades.size(); i++) {
        if (grades[i] < 38) newGrades.push_back(grades[i]);
        else {
            int nextMult = ceil(grades[i] / 5.0) * 5;
            if (fabs(nextMult - grades[i]) < 3) newGrades.push_back(nextMult);
            else newGrades.push_back(grades[i]);
        }
    }
    return newGrades;
}

int main() {
    vector<int> inpt;
    inpt.push_back(73);
    inpt.push_back(67);
    inpt.push_back(38);
    inpt.push_back(33);
    cout << ceil(73.0 / 5) << endl;
    for (int x : inpt) {
        cout << x << " ";
    }
    cout << endl;
    vector<int> ans = gradingStudents(inpt);
    for (int x : ans) {
        cout << x << " ";
    }
    cout << endl;
}