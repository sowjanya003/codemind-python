n=int(input())
l=list(map(int,input().split()))
l1=[]
if n%2==0:
    l1=l
    print(*l1)
else:
    l1=l
    l1.append(0)
    print(*l1)