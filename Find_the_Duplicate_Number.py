n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if l.count(i)>1:
        l1.append(i)
print(max(l1))