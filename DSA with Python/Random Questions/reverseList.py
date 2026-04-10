def reverse(arr):
    reversed_arr = []
    n = len(arr) - 1
    for _ in range(len(arr)):
        reversed_arr.append(arr[n])
        n-=1
    return reversed_arr

arr = [1,2,2,4]
print(reverse(arr))