n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1 and l.count(i)==i:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    mn=min(l1)
    mx=max(l1)
    print(mn,mx)
