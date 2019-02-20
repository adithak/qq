l=int(input("enter l"))
k=int(input("enter k"))
i=1
j=0
c=0
while(j<k):
    print(1,end='')
    c=c+1
    while(i<=l and c==2):
        print(0,end='')
        c=0
        i+=1
        break
    if c==2:
        break
    j+=1
if i!=l+1 or j+1!=k:
    print("\ncannot")
