n=5
count = n

for i in range(1,n+1):
    for j in range(count,0,-1):
        print(i,end=' ')
    count-=1
    print(end='\n')