# defining a list
list1 = []

# take the input from user regarding 
n = int(input('Enter number of elements you want in the list : '))

for i in range(0,n):
    num = int(input(f'Enter element number {i} : '))
    list1.append(num)

print(f'The original list user entered: {list1}')

# Sorting the list without list() 
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] >= list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(f'The original list user entered: {list1}')