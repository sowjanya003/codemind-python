n=int(input())
l=list(map(int,input().split()))
l.sort()
l1=[]
for i in l:
    k=i**2
    l1.append(k)

l1.sort()
print(*l1)