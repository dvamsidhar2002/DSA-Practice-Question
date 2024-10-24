# defining a list
list1 = []

def cyclically_rotate(listr,k):
    n = len(listr)
    
    # Normalize k to avoid rotating more than necessary (handle cases where k > n)
    k = k % n
    
    # Step 1: Slice the last k elements and the first n-k elements
    rotated_array = listr[-k:] + listr[:-k]
    
    return rotated_array

if __name__=="__main__":

    # take the input from user regarding 
    n = int(input('Enter number of elements you want in the list : '))
    k = int(input('Enter the value to rotate the list by that number : '))
    for i in range(0,n):
        num = int(input(f'Enter element number {i} : '))
        list1.append(num)

    print(f'The original list user entered: {list1}')

    cyclically_rotated_list = cyclically_rotate(list1,k)

    print(f'Cyclically Rotated the list by {cyclically_rotated_list}')

