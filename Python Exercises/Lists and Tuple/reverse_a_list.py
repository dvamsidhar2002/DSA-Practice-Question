# taking the size of the list from user
n = int(input('Enter the size of the list according to you : '))
list1 = []

# taking the list elements as input from user/during runtime
print(f'Enter {n} elements : ')
for i in range(n):
    element = int(input())
    list1.append(element)

print(f'Original list: {list1}')

print(f'Reversed list : {list1[::-1]}')
