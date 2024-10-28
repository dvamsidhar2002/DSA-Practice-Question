#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string str, reversed_str;
    int count = 0;
    cout<<"Enter a string of your choice : ";
    getline(cin, str);

    int n = str.length();

    for (char &ch : str) {
        if (std::islower(ch)) {
            ch = std::toupper(ch);
        }}

    reversed_str = str;

    for (int i = 0; i < n / 2; i++){
        char temp = reversed_str[i];
        reversed_str[i] = reversed_str[n - i - 1];
        reversed_str[n - i - 1] = temp;
    }

    for (int i=0;i<n;i++)
    {
        if(str[i]==reversed_str[i])
        {
            count+=1;
        }
    }

    if(count==n) {cout<<"This string is palindrome.";}
    else {cout<<"This string is not palindrome.";}

    return 0;
}