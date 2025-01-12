if __name__=="__main__":
    N = int(input('Enter the number of towers in an array: '))
    list1 = []
    print(f'Enter {N} heights into the array : ')

    for i in range(N):
        a = int(input())
        list1.append(a)
    k = int(input('Enter the number by which height should be increased or decreased : '))
    for i in range(N):
        action = str(input(f'Enter I to increase or D to decrease the height of tower {i} : '))
        if action == 'I' or action == 'i':
            list1[i] += k
        elif action == 'D' or action == 'd':
            list1[i] -= k
    
    list1.sort()
    print(list1[N-1] - list1[0])
