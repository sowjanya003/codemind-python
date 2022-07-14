n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i<0:
        i=str(-i)
    else:
        i=str(i)
    s=str(i)
    k=len(s)
    print(k,end=' ')