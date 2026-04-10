def mergeSortedList(arr1, arr2):
    i, j = 0, 0
    result = []
    
    print(f"Initial arrays:\narr1 = {arr1}\narr2 = {arr2}\n")
    
    while i < len(arr1) and j < len(arr2):
        print(f"Comparing arr1[{i}] = {arr1[i]} and arr2[{j}] = {arr2[j]}")
        
        if arr1[i] < arr2[j]:
            print(f"→ Taking {arr1[i]} from arr1")
            result.append(arr1[i])
            i += 1
        else:
            print(f"→ Taking {arr2[j]} from arr2")
            result.append(arr2[j])
            j += 1
        
        print(f"Current result: {result}\n")
    
    # Remaining elements in arr1
    while i < len(arr1):
        print(f"arr2 exhausted, adding remaining arr1[{i}] = {arr1[i]}")
        result.append(arr1[i])
        i += 1
        print(f"Current result: {result}\n")
    
    # Remaining elements in arr2
    while j < len(arr2):
        print(f"arr1 exhausted, adding remaining arr2[{j}] = {arr2[j]}")
        result.append(arr2[j])
        j += 1
        print(f"Current result: {result}\n")
    
    print(f"Final merged array: {result}")
    return result

arr1 = [1,3,6]
arr2 = [2,4,5]
print(mergeSortedList(arr1, arr2))