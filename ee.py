m=input()
l=input()
temp=str(m)
temp2='0'*l
val=m
pwr=10
if l>0:
	while 1:
		if temp[len(temp)-l:len(temp)]==temp2 and val%n==0:
			break
		else:
			val=m*pwr
			temp=str(val)
			pwr+=10

print val
