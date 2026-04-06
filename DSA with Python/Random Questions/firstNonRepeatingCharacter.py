def firstNonRepeatingCharacter(string):
    seen = {}
    for i in range(len(string)):
        if string[i] in seen:
            seen[string[i]]+=1
        else:
            seen[string[i]]=1
    
    for key, value in seen.items():
        if value==1:
            return key
    
    return 'Invalid String'


string = 'aabbcde'
print(firstNonRepeatingCharacter(string))