string = str(input('Enter a string of your choice : '))
string = string.lower()
duplicates = []

for i in range(0,len(string)):
    for j in range(i+1,len(string)):
        if string[i] == string[j]:
            duplicates.append(string[i])

duplicates = set(duplicates)

print(f'Duplicates in the entered string : {duplicates}')