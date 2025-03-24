n=6
count=n

for i in range(0,n+1):
    i = 0
    for j in range(count,0,-1):
        print(i, end=' ')
        i+=1
    count-=1
    print(end='\n')