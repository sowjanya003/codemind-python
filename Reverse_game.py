n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
        s=str(l[i])
        k=s[::-1]
        l1.append(int(k))
print(*l1)