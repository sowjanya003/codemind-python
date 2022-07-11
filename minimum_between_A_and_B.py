n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
p=[]
for i in range(n):
    if (a<=l[i]<=b):
        p.append(l[i])
if len(p)==0:
    print(-1)
else:
    print(min(p))
        