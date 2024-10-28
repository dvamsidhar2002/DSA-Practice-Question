#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<char> list1;  // Define a vector to store elements
    int n;

    // Take the input from user regarding number of elements
    cout << "Enter number of elements you want in the array: ";
    cin >> n;

    // Loop to take elements from user
    for (int i = 0; i < n; ++i) {
        char num;
        cout << "Enter element number " << i << ": ";
        cin >> num;
        list1.push_back(num);
    }

    // Display the original array
    cout << "The original array user entered: ";
    for (int i = 0; i < n; ++i) {
        cout << list1[i] << " ";
    }
    cout << endl;

    // Display the reversed array
    cout << "The reversed array: ";
    for (int i = n - 1; i >= 0; --i) {
        cout << list1[i] << " ";
    }
    cout << endl;

    return 0;
}
