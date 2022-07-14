n,k=map(int,input().split())
l=list(map(int,input().split()))

c=0

for i in l:
    if i<0:
        i=str(-i)
    else:
        i=str(i)
    if len(i)==k:
        c+=1
print(c)
    