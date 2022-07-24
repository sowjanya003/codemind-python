n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(n//2):
    l1.append(l[i])
for j in range(n//2,n):
    l2.append(l[j])
l2.reverse()
l3=l2+l1
print(*l3)