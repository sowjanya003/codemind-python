n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in l:
    if i not in l1 and i%2:
        c+=1
        l1.append(i)
print(sum(l1))