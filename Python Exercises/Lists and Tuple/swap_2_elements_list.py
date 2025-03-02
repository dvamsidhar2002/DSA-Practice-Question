n = int(input('Enter the size of the list according to you : '))
list1 = []
print(f'Enter {n} elements : ')
for i in range(n):
    element = int(input())
    list1.append(element)

print(f'Original list: {list1}')

index1 = int(input('Enter 1st index number:'))
index2 = int(input('Enter 2nd index number:'))

temp = list1[index1]
list1[index1] = list1[index2]
list1[index2] = temp

print(f'Updated list: {list1}')