n=input()
l=list(n.split())
v='aeiou'
l1=[]
l2=[]
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    l1.append(c)
for k in l1:
    l2.append(k)
print(min(l2))