n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
for i in range(n):
    if not(x<=l[i]<=y):
        s+=l[i]
print(s)