n = 5
p = 65

for i in range(1, n+1):
    for j in range(i):
        print(chr(p),end=' ')
        p+=1
    print(end='\n')