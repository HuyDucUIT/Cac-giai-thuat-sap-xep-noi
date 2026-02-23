#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main() {
    ifstream file("data.csv");
    string line, val;
    getline(file, line); 

    vector<vector<double>> data(10);
    while (getline(file, line)) {
        stringstream ss(line);
        for (int i = 0; i < 10; i++) {
            getline(ss, val, ',');
            data[i].push_back(stod(val));
        }
    }

    auto s2 = high_resolution_clock::now();
    for (int i = 0; i < 10; i++) {
        auto s = high_resolution_clock::now();
        sort(data[i].begin(), data[i].end());
        auto e = high_resolution_clock::now();
        cout << "Day " << i + 1 << ": " << duration<double, milli>(e - s).count() << " ms" << endl;
    }
    auto e2 = high_resolution_clock::now();
    cout << "Trung binh: " << duration<double, milli>(e2 - s2).count() / 10 << " ms" << endl;
    return 0;
}