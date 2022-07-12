n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n+1):
    if i<=n/2:
        a.append(i)
    if i>n/2:
        b.append(i)
print(abs(sum(a)-sum(b)))