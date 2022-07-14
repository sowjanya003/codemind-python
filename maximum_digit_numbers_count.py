n=int(input())
l=list(map(int,input().split()))
a=[]
k=max(l)
for i in l:
    if len(str(i))>0:
        a.append(len(str(i)))
m=max(a)
for i in l:
    if len(str(i))==m:
        print(i,end=' ')