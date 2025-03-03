n = int(input('Enter the size of the list : '))
list1 = []
print(f'Enter {n} elements into the list : ')
for i in range(n):
    element = int(input())
    list1.append(element)

output_list1 = []

for i in range(n):
    element = pow(list1[i],2)
    output_list1.append(element)

print(f'Original List : {list1}')
print(f'Squared List : {output_list1}')