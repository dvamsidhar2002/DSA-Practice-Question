if __name__=="__main__":

    # take the input from user regarding 
    first = 0
    second = 1
    n = int(input('Enter how many numbers in a Fibonacci series you want: '))
    print(first,second,end=' ')
    for i in range(0,n):
        third = first + second
        first = second
        second = third
        print(third,end=' ')