string=input()
flag=1
for i in range(len(string)):
    if string[i] != string[-1-i]:
        flag=0
if(flag==1):
    print("YES")
else:
    print("NO")
        
