def sumOfElementsinArray(arr):
    return sum(arr)

def manual_technique(arr):
    sum = 0
    for i in range(len(arr)):
        sum+=arr[i]    
    return sum

arr = [1,2,3,4]
print(sumOfElementsinArray(arr))
print(manual_technique(arr))