# taking the size of the list from user
n = int(input('Enter the size of the list according to you : '))
list1 = []

# taking the list elements as input from user/during runtime
print(f'Enter {n} elements : ')
for i in range(n):
    element = int(input())
    list1.append(element)

print(f'Original list: {list1}')

# Occurence counting
occ = int(input('Enter the element whose occurrences you want to count : '))
count = 0

for i in range(n):
    if list1[i] == occ:
        count+=1

print(f'Element {occ} has occured {count} times.')