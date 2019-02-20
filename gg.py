c1=input()
c2=input()
s=1
for y in range(4,min(len(c1),len(c2))+1):
    if (len(c1)%y==0 and len(c2)%y==0):
          s=s+1
print(s)    
