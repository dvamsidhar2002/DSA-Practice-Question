def binary_palindrome(num):
    number = [int(digit) for digit in str(num[0])]
    i,j = 0, len(number)-1
    isPalindrome = True

    while i<j:
        if number[i]!=number[j]:
            isPalindrome=False
            break
        i+=1
        j-=1

    return isPalindrome

if __name__ == '__main__':
    num = [int(input('Enter the binary number : '))]
    results = binary_palindrome(num)

    if results==True:
        print('The binary number is a palindrome.')
    else:
        print('The binary number is not a palindrome.')