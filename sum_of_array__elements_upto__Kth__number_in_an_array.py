n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in l:
    if i==k:
        a.append(k)
        break
    else:
        a.append(i)
print(sum(a))
    