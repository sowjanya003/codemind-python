n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in l:
    if i not in l1 and l.count(i)==i:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    s=sum(l1)
    avg=s/len(l1)
    print("%0.2f"%avg)