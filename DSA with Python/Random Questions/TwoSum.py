def twoSum(arr,target):
    seen = {}
    for i in range(len(arr)):
        needed = target - arr[i]
        if needed in seen:
            return seen[needed],i
        seen[arr[i]] = i
    return 'No Valid Elements'

arr = [0,2,5,1,9]
target = 9

print(twoSum(arr,target))