n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,n,2):
    #n.append(l[i])
    #print(a)
    for j in range(0,l[i+1]):
        a.append(l[i])
print(*a)