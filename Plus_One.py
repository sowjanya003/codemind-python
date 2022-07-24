n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    l1.append(str(i))
l2=''.join(l1)
l3=int(l2)+1
l4=str(l3)
l5=' '.join(l4)
print(l5)