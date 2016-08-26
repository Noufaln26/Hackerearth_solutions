test=int(input())
count=0
for i in range(test):
    N=int(input())
    for j in range(1,N+1):
        for k in range(j+1,N+1):
            if((j ^ k) <= N):
                count+=1
print(count)
