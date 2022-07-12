n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=a+b
for i in a:
    if i in a and i not in b:
        c.append(i)
for j in b:
    if j in b and j not in a:
        c.append(j)
print(*c)