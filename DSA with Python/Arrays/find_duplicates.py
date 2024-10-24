def find_duplicates(arr,k):

    duplicate_elements = []

    for i in range(0,k+1):
        for j in range(i+1,k+1):
            if arr[i] == arr[j]:
                duplicate_elements.append(arr[i])

    return duplicate_elements

if __name__ == "__main__":
    # defining a list
    list1 = []

    # take the input from user regarding
    n = int(input('Enter number of elements you want in the list : '))

    for i in range(0, n+1):
        num = int(input(f'Enter element number {i} : '))
        list1.append(num)

    print(f'The original list entered by user : {list1}')

    duplicates = find_duplicates(list1,n)

    print(f'Duplicate elements in list are : {duplicates}')