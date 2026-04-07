def LCM(num1, num2):
    arr1 = set()
    arr2 = set()
    for i in range(1, max(num1, num2)+1):
        arr1.add(num1*i)
        arr2.add(num2*i)

    return min(list(arr1 & arr2))

def greatestCommonDivisor(num1, num2):
    gcd = 1
    for i in range(1, min(num1, num2)):
        if num1%i==0 and num2%i==0:
            gcd = i
    return gcd

def efficient_LCM(num1, num2):
    return abs(num1 * num2)//greatestCommonDivisor(num1, num2)

num1 = 4
num2 = 1
print(efficient_LCM(num1, num2))