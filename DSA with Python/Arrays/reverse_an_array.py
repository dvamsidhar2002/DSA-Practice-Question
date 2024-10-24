# defining a list
list1 = []

# take the input from user regarding 
n = int(input('Enter number of elements you want in the list : '))

for i in range(0,n):
    num = int(input(f'Enter element number {i} : '))
    list1.append(num)


print(f'The original list user entered: {list1}')
print('\n')
print(f'The reversed list {list1[::-1]}')