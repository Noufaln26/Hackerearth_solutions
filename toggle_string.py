name=input()
s=''
for c in name:
    if c.isupper():
        s+=c.lower()
    else:
        s+=c.upper()
print(s)        
    
