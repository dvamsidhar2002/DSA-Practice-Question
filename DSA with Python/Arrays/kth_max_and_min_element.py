# defining a list
list1 = []

# take the input from user regarding 
n = int(input('Enter number of elements you want in the list : '))

for i in range(0,n):
    num = int(input(f'Enter element number {i} : '))
    list1.append(num)

print(f'The original list user entered: {list1}')

k = int(input('Enter which kth max and min element you want to print from the above list : '))
list1.sort()
print(f'{k}th Maximum Value : {list1[n-k]}, {k}th Minimum Value : {list1[k-1]}')
print('\n\n')