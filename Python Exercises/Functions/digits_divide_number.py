def digits_divide_number(num):
    numbers = [int(digit) for digit in str(num[0])]
    canDivide = True
    for i in numbers:
        if num[0]%i!=0:
            canDivide = False
            break

    return canDivide

if __name__ == '__main__':
    num = [int(input('Enter any number of your choice : '))]
    results = digits_divide_number(num)

    if results == True:
        print('Yes! all digits of the number divide it.')
    else:
        print('No! all digits of the number don\'t divide it.')