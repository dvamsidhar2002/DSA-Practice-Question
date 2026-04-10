def findDuplicates(arr):
    seen = {}
    for i in arr:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    
    duplicates  = []
    for key, value in seen.items():
        if value>1:
            duplicates.append(key)
    return duplicates

arr = [1,2,3,4,5,2,5]
print(findDuplicates(arr))