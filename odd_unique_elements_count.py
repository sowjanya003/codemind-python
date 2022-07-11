n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
s=0
for i in l:
    if i not in l1 and i%2:
        l1.append(i)
        c+=1
print(c)