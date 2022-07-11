n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in range(n):
    if (a<=l[i]<=b):
        k.append(l[i])
if len(k)==0:
    print(-1)
else:
    print(max(k))