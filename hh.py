b,v=map(int,input().split())
v1=list(map(int,input().split()))
v2=list(map(int,input().split()))
c1=0
c2=0
for x in range(0,len(v1)):
    c1=c1+v1[x]
    c2=c2+v2[x]
print(c2//c1)
