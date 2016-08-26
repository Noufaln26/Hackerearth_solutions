T=int(input())
c=list()
new=list()
for i in range(T):
    N=int(input())
    array=map(int,input().split(" "))
    for i  in array:
        count=bin(i).count("1")
        c.append(count)
   
