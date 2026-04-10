def twoSum(arr, target):
    seen = set()
    result = []
    for i in range(len(arr)):
        #print(seen)
        if target - arr[i] in seen:
            result.append((arr.index(target - arr[i]), i))
        else:
            seen.add(arr[i])
        
    return result

arr = [1, 2, 3, 4, 3]
target = 6
print(twoSum(arr, target))