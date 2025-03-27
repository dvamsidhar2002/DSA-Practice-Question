def factorial_number(num):
    fact = 1

    for i in range(1,num+1):
        fact=fact*i
    return fact

if __name__ == '__main__':
    num = int(input('Enter the number whose factorial you need : '))
    fact = factorial_number(num)

    print(f'Factorial of {num} is: {fact}')