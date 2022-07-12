n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
k=0
for i in a:
    if i in b and i not in c:
        c.append(i)
for j in c:
    if j in a:
        k+=1
print(k)