n = int(input('Enter the size of the list : '))
print(f'Enter {n} elements : ')
list1 = [int(input()) for _ in range(n)]  # Directly creating the list

search = int(input('Enter the element you want to be deleted : '))

# Create a new list excluding the searched element
list1 = [x for x in list1 if x != search]

print(f'Updated list : {list1}')
