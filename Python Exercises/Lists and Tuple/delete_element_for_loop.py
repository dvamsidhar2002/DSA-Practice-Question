n = int(input('Enter the size of the list : '))
list1 = []
print(f'Enter {n} elements into the list : ')
for i in range(n):
    element = int(input())
    list1.append(element)

search = int(input('Enter the element you want to be deleted : '))

output_list = []
for i in range(n):
    if list1[i] != search:
        output_list.append(list1[i])

print(f'Original List : {list1}')
print(f'Updated List : {output_list}')