def isPalindrome(string: str):
    # string = string.lower()  If case doesn't matter
    left, right = 0, len(string) - 1
    while left < right:
        if string[left]!=string[right]:
            return 'Not a Palindrome'
        left+=1
        right-=1
    return 'It is a Palindrome'

string = 'Madam'
print(isPalindrome(string))