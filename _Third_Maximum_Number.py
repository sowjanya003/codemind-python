n=int(input())
l=list(map(int,input().split()))
l.sort()
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
if(len(l1)<3):
    print(max(l1))
else:
    print(l1[len(l1)-3])
    