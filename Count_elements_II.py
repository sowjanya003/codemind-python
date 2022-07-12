n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
k=0
for i in a:
    if i not in b and i not in c:
        k+=1
        c.append(i)
for j in b:
    if j not in a and j not in c:
        k+=1
        c.append(j)
        
print(k)