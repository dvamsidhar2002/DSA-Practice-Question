n = int(input('Enter the size of the list according to you : '))
list1 = []
print(f'Enter {n} elements : ')
for i in range(n):
    element = int(input())
    list1.append(element)

print(f'Original list: {list1}')

temp = list1[n-1]
list1[n-1] = list1[0]
list1[0] = temp

print(f'Updated list: {list1}')