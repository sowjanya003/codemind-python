def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True

n=int(input())
l=list(map(int,input().split()))
m1=l.index(min(l))
m2=l.index(max(l))
c=0
if m1>m2:
    m1,m2=m2,m1
for i in range(m1,m2+1):
    if prime(l[i]):
        c+=1
print(c)