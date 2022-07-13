n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    s=0
    for j in str(i):
        s+=int(j)
    a.append(s)
print(sum(a))