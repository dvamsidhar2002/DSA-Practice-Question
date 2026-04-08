import numpy as np

def averageOfNumbers(arr):
    return int(np.mean(arr))

def manual_technique(arr):
    return int(sum(arr)/len(arr))

arr = [2,4,6,8]
print(averageOfNumbers(arr))
print(manual_technique(arr))