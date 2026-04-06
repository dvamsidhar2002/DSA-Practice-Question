def reverseAnInteger(num):
    sign = -1 if num < 0 else 1
    reverse = int(str(abs(num))[::-1])
    return sign * reverse

num = -123
print(reverseAnInteger(num))