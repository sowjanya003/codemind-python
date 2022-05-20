n=int(input())
l=list(map(int,input().split()))
d=[]
e=[]
for i in range(n):
    if l[i]%2!=0:
        d.append(l[i])
    if l[i]%2==0:
        e.append(l[i])
    k=d+e
print(*k)