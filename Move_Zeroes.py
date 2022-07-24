n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in l:
    if i!=0:
        l1.append(i)
    else:
        l2.append(i)
        
l3=l1+l2
print(*l3)