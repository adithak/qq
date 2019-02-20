q,e=input().split()
count=0
q=set(q)
e=set(e)
for i in q:
    if i in e:
        count=count+1
if(count>=2):
    print('yes')
elif(count<2):
    print('no')
