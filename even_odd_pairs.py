n=int(input())
l=list(map(int,input().split()))
e=[]    
o=[]
c=len(l)
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
k=[]
r=0
if len(o)==len(e):
    for i in range(len(o)):
        k.append(e[i])
        k.append(o[i])
    print(*k)
elif len(o)>len(e):
    r=o[len(e)::]
    for i in range(len(e)):
        k.append(e[i])
        k.append(o[i])
    if len(r)%2!=0:
        r.append(0)
    k=k+r
    print(*k)
elif len(e)>len(o):
    r=e[len(o)::]
    for i in range(len(o)):
        k.append(e[i])
        k.append(o[i])
    if len(r)%2!=0:
        r.append(0)
    k=k+r
    print(*k)
