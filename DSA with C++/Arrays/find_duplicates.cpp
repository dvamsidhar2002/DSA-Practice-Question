#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> arr;
    int n, num, i, j;

    cout<<"Enter the size of the string : ";
    cin>>n;

    for(i=0;i<n;i++)
    {
        cout<<"Enter the element number "<<i<<" :";
        cin>>num;

        arr.push_back(num);
    }

    cout<<"\nThe array given by user : ";
    for(i=0;i<n;i++)
    {cout<<arr[i]<<" ";}

    cout<<"\nDuplicate Elements in the array : ";

    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(arr[i]==arr[j])
            {
                cout<<arr[i]<<" ";
            }
        }
    }


    return 0;
}