n=input()
l=list(n.split())
v='aeiou'
l1=[]
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    l1.append(c)
l2=[]
for k in l1:
    if k==max(l1):
        l2.append(k)
print(len(l2))