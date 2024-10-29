#include<iostream>
#include<vector>
using namespace std;

int main()
{
    vector<int> arr;
    int n,num,k;

    // Taking size of array from user 
    cout<<"Enter the number of elements in an array : ";
    cin>>n;

    // Taking the elements input from user
    for (int i=0 ; i<n ; i++)
    {
        cout<<"Enter element number "<<i<<":";
        cin>>num;
        arr.push_back(num);
    }

    // Display the original array
    cout << "The original array user entered: ";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // creating a temporary variable;
    int temp;

    // Sorting the array - SELECTION SORT
    for (int i=0 ; i<n ; i++)
    {
        for (int j=i+1 ; j<n; j++)
        {
            if(arr[i]>arr[j])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    cout<<"Enter the value of k, this will display kth maximum and minimum element from the array : ";
    cin>>k;

    // Display Maximum and minimum elements of the array 
    cout << "Minimum element : "<<arr[k-1]<<" Maximum element : "<<arr[n-k];


}