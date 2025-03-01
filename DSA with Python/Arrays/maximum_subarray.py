import sys

def maxSubarraySum(arr, n):
    max_so_far = -sys.maxsize - 1

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            max_so_far = max(max_so_far, sum)

    return max_so_far

if __name__ == '__main__':
    arr = []
    n = int(input('Enter the number of elements you want in the array : '))
    print(f'Enter {n} elements :')
    for i in range(n):
        element = int(input())
        arr.append(element)
    maxSum = maxSubarraySum(arr, n)
    print("The maximum subarray sum is:", maxSum)