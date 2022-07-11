n=int(input()) 
l=list(map(int,input().split()))

c=0
l1=[]

for i in l:
    if i not in l1:
        c+=1
        l1.append(i)
print(sum(l1))