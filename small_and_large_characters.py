n=input()
l=n.split()
for i in range(len(l)):
    k=min(l[i])
    p=max(l[i])
    print(k,p,end=' ')