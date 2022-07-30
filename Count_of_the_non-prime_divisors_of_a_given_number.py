def npd(a):
    c=0
    d=0
    for j in range(1,a+1):
        if a%j==0:
            c+=1
    if c!=2:
        d+=1
    return d
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(npd(i))
print(sum(l))