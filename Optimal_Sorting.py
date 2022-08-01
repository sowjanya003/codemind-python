n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    k=sorted(l)
    if l==k:
        print(0)
    else:
        print(max(k)-min(k))