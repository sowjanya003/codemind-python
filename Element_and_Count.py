n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    print(i,l.count(i),end=' ')