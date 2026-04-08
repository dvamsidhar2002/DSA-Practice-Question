def countEvenOdd(arr):
    even_count = 0
    for i in range(len(arr)):
        if arr[i]%2==0:
            even_count+=1

    return f'Even Count:{even_count}, Odd Count:{len(arr)-even_count}' 

arr = [1,2,0,4,5]
print(countEvenOdd(arr))