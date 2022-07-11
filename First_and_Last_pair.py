n=int(input())
l=list(map(int,input().split()))
i=0
l1=[]
while i!=n//2:
    l1.append(l[i])
    l1.append(l[(n-1)-i])
    i+=1
if len(l)%2!=0:
    l1.append(l[i])
    l1.append(0)
print(*l1)