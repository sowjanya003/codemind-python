n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in range(n):
    if i%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
        
s=sum(o)-sum(e)
if s==0:
    print('YES')
else:
    print('NO')