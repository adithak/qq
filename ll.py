m = int(input())
l = 3
b = l
while(n>0):
    if(b == 0):
        l = 2*l
        b = l
    if(m==1):
        print(b)
        break
    m -= 1
    b -= 1
