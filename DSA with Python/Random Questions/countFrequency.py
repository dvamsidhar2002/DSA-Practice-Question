def value_counts(arr):
    seen = {}
    for i in arr:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1

    return seen

arr = [1,2,3,4,5,6,1,2,3]
print(value_counts(arr))