n=int(input())
l=list(map(int,input().split()))
a=max(l)
c=0
for i in l:
    if len(str(a))==len(str(i)):
        c+=1
print(c)