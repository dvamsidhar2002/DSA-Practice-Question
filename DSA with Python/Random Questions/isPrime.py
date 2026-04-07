import math
def isPrime(num):
    if num<2:
        return 'Not a Prime Number'
    
    for i in range(2, num):
        if num%i==0:
            return 'Not a Prime Number'
    return 'Prime Number'

num = 4
print(isPrime(num))