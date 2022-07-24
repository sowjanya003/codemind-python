n=int(input())
l=list(map(int,input().split()))
a=int(input())
for i in range(n):
    if l[i]==a:
        print(i,end=" ")
        break
else:
    print(-1,end=" ")
for i in range(n-1,-1,-1):
    if l[i]==a:
        print(i)
        break
else:
    print(-1)