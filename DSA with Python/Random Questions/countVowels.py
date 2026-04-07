def countVowels(string: str):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range(len(string)):
        if string[i] in vowels:
            count+=1
    return count

string = 'Vamsidhar'
print(countVowels(string))