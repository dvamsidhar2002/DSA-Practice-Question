name = 'Python'
list1 = list(name)
n = len(list1)

for i in range(1,n+1):
    for j in range(i):
        print(list1[j], end=' ')
    print(end='\n')