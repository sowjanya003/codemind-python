n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=-1
for i in range(0,n):
    if l[i]==k:
        c=i
        break
print(c)