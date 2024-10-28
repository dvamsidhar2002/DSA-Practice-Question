#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string str;

    cout<<"Enter a string : ";
    getline(cin, str);

    int n = str.length();

    for (int i = 0; i < n / 2; i++) {
        // Swap characters from the beginning and end
        char temp = str[i];
        str[i] = str[n - i - 1];
        str[n - i - 1] = temp;
    }

    cout<<"Reversed String : "<<str;

    return 0;
}