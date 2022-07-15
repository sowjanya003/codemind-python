n=input()
s=list(n.split())
l1=[]
l2=[]
l3=[]
for i in s:
    k=max(i)
    l1.append(k)
    p=min(i)
    l1.append(p)
    for j in i:
        l2.append(j)

mi=min(l1)
ma=max(l1)
cmi=l2.count(mi)
cma=l2.count(ma)
print(mi,cmi,ma,cma,end=' ')