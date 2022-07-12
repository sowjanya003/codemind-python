n,m=map(int,input().split())
N=list(map(int,input().split()))
M=list(map(int,input().split()))
s=N+M
a=[]
for i in N:
    if i in M and i not in a:
        a.append(i)
        
print(*a)