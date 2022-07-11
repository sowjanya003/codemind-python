n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    if l.count(i)==i:
        c=1
        print(i,end=' ')
if c==0:
    print(-1)
    