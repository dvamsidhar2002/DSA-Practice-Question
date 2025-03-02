n = int(input('Enter the size of the list '))
list1 = []

print(f'Enter {n} elements into the list : ')
for i in range(n):
    element = int(input())
    list1.append(element)

print(f'Original List: {list1}')

list1.sort()

print(f'Smallest element from the list: {list1[0]} and largest element from the list : {list1[n-1]}')