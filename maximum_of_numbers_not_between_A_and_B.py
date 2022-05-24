n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in range(n):
    if not(a<=l[i]<=b):
        d.append(l[i])
if len(d)==0:
    print(-1)
else:
    print(max(d))