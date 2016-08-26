L=int(input())
testcase=int(input())
for i in range(testcase):
    w,h=map(int,input().split(" "))
    if((w<L) or (h<L)):
        print("UPLOAD ANOTHER")
    elif(((w>L) or (h>L)) and w==h):
         print("ACCEPTED")
    elif((w>L) or (h>L)):
         print("CROP IT")
    else:
         print("ACCEPTED")
    
