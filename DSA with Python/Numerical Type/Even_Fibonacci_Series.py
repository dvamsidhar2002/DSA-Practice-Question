if __name__=="__main__":

    # take the input from user regarding 
    first = 0
    second = 1
    n = int(input('Enter how many numbers in a Fibonacci series you want: '))
    if first%2==0:
        print(first,end=' ')
    elif second%2==0:
        print(second,end=' ')

    for i in range(0,n):
        third = first + second
        first = second
        second = third
        if third%2==0:
            print(third,end=' ')