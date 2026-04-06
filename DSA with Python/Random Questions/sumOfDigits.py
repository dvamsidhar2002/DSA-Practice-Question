def sumOfDigits(num):
    if num==0:
        return num
    quotient = num//10
    rem = num%10
    return rem + sumOfDigits(quotient)

num = 678
print(sumOfDigits(num))