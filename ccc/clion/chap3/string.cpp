//
// Created by Michael Nath on 12/25/19.
//

#include <iostream>
#include <string>
using std::endl; using std::cout; using std::cin; using std::string;
int main() {
    string smth;
    string monkey = "Monkey";
    string copy(monkey);
    cout << monkey << copy << "\n" << smth.empty() << "\n" << monkey.empty() << endl;
    cout << "size of monkey is " << monkey.size() << endl;
//    The below lines of code requires two string variables to capture the name.
//    Can't be used for names more than 2 words.
//    string n1, n2;
//    cout << "What is your name?" << endl;
//    cin >> n1 >> n2;
//    cout << n1 << "\t" << n2 << endl;
    string name;
    cout << "What is your name?" << endl;
    getline(cin, name);
    string dup(name);
    dup += monkey;
    cout << name << dup << endl;

    return 0;
}