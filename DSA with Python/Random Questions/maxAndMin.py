def maxAndmin(arr):
    maxi = mini = arr[0]
    for i in arr:
        if i>maxi:
            maxi=i
        elif i<mini:
            mini=i

    return f'Maximum Element : {maxi}, Minimum Element: {mini}'

arr = [1,4,7,8,2,-1,3]
print(maxAndmin(arr))