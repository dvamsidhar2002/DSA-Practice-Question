n = int(input('Enter the size of the list according to you : '))
list1 = []
print(f'Enter {n} elements : ')
for i in range(n):
    element = int(input())
    list1.append(element)

list1.sort()

print(list1[n-1])