n = 6
count = n

for i in range(1,n+1):
    for j in range(count,0,-1):
        print(n, end=' ')
    n-=1
    count-=1
    print(end='\n')