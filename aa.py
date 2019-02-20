m,q = input().split()
m,q = int(m),int(q)
L = [int(x) for x in input().split()]
L.sort()
out = 0
a = m // 3
for i in range(0,a) :
    L2 = L[3*i : 3*(i+1)]
    if 5-max(L2) >= q :
        out += 1
print(out)
