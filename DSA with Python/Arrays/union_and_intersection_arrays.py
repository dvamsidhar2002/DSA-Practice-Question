# defining two lists
list1 = []
list2 = []

# take the input from user regarding 
n = int(input('Enter number of elements you want in the list : '))


# Enter values in both the lists
for i in range(0,n):
    num = int(input(f'Enter element number {i} : '))
    list1.append(num)

for i in range(0,n):
    num = int(input(f'Enter element number {i} : '))
    list2.append(num)

print(f'The original list 1 user entered: {list1}')
print(f'The original list 2 user entered: {list2}')

list1.sort()
list2.sort()

print(f'\nSorted list 1 : {list1}')
print(f'\nSorted list 2 : {list2}')

intersection = []

for i in range(0,n):
    for j in range(0,n):
        if list1[i] == list2[j]:
            intersection.append(list1[i])

print(f'The intersection of two lists : {intersection}')


# Find the union of two lists
union = list(set(list1) | set(list2))

print(f'The union of two lists : {union}')