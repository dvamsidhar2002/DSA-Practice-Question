def intersectionOfTwoArrays(arr1, arr2):
    common = set()
    if len(arr1)<len(arr2):
        for i in range(len(arr2)):
            if arr2[i] in arr1:
                common.add(arr2[i])
        return common
    else:
        for i in range(len(arr1)):
            if arr1[i] in arr2:
                common.add(arr1[i])
        return common

arr1 = [1,2,2,1]
arr2 = [2,2]

print(intersectionOfTwoArrays(arr1, arr2))