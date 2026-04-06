def move_zeroes_to_one_side(arr):
    zeroes = []
    non_zeroes = []

    result = []
    for i in range(len(arr)):
        if arr[i]==0:
            zeroes.append(arr[i])
        else:
            non_zeroes.append(arr[i])
        
    result = zeroes + non_zeroes
    return result

arr = [0,1,0,3,12]
print(move_zeroes_to_one_side(arr))