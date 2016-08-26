L,R,K= map(int,input().split(" "))
print("{}".format(len([i for i in range(L,R+1) if i%K==0])))
