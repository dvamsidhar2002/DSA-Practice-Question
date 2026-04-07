def factorial(num):
    if num==1:
        return num
    elif num==0:
        return 1
    n = num-1
    return num * factorial(n)

num = 0
print(factorial(num))