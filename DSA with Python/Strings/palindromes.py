string = str(input('Enter a string of your choice : '))

print(f'String entered by the user : {string}')
print(f'Reversed string : {string[::-1]}')
string = string.lower()
reversed_string = string[::-1]

#counter to verify
count = 0

for i in range(0,len(string)):
    if string[i] == reversed_string[i]:
        count+=1

if count == len(string):
    print('Yes! the input given by user is a palindrome')
else:
    print('No! the input given by user is not a palindrome')