n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i%k==0:
        b.append(i)
        c+=1
print(c)