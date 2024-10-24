# defining a list
list1 = []

# take the input from user regarding 
n = int(input('Enter number of elements you want in the list : '))

for i in range(0,n):
    num = int(input(f'Enter element number {i} : '))
    list1.append(num)

print(f'The original list user entered: {list1}')


# Sorting the list and printing the maximum and minimum values in the list
list1.sort()
print(f'Maximum Value : {list1[n-1]}, Minimum Value : {list1[0]}')