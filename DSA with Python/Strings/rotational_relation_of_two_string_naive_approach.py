def naive_approach(string1, string2):
    l1 = len(string1)
    rotated_string = []

    for k in range(1,l1+1):
        k = k%l1
        rotated = string1[-k:]+string1[:-k]
        rotated_string.append(rotated)

    for rotated in rotated_string:
        if rotated == string2:
            return True

    return False


if __name__ == '__main__':
    s1 = str(input('Enter first string : '))
    s2 = str(input('Enter second string : '))

    # Naive Approach
    naive_result = naive_approach(s1,s2)
    print("----------NAIVE APPROACH----------")
    print("True: if s2 is rotation of s1; False: if s2 is not rotation of s1")
    print(naive_result)
