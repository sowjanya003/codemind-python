n=input()
l=n.split()
l1=[]
for i in l:
    l2=i[::-1]
    l1.append(l2)
print(*l1)