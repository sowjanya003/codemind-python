l=list(map(int,input().split()))
#print(l)
l1=max(l)
for i in range(len(l)):
    if l[i]==max(l):
        l[i]=0
        break
l2=max(l)
l3=(l1-1)*(l2-1)
print(l3)