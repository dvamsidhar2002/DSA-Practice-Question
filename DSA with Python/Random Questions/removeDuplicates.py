def removeDuplicates(arr):
    seen = set()
    result = []
    for i in range(len(arr)):
        if arr[i] in seen:
            continue
        else:
            seen.add(arr[i])
            result.append(arr[i])
    
    return result

arr = [1,2,6,2,4,5,1]
print(removeDuplicates(arr))