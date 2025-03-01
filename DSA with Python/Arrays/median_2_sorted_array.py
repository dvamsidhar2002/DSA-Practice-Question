def median_sorted_array(arr1, arr2, n1, n2):
    arr = []
    for i in arr1:
        arr.append(i)

    for j in arr2:
        arr.append(j)

    arr.sort()

    n = len(arr)

    if n%2!=0:
        return arr[n//2]
    else:
        return (arr[(n//2)-1] + arr[n//2])/2


if __name__ == '__main__':
    n1 = int(input('Enter the number of elements in the array 1 : '))
    n2 = int(input('Enter the number of elements in the array 2 : '))
    arr1 = []
    arr2 = []
    print(f'Enter {n1} elements for array 1 : ')
    for i in range(n1):
        element = int(input())
        arr1.append(element)
    print(f'Enter {n2} elements for array 2 : ')
    for i in range(n2):
        element = int(input())
        arr2.append(element)

    median = median_sorted_array(arr1, arr2, n1, n2)
    print(median)