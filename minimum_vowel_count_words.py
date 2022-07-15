n=input()
l=list(n.lower().split())
#print
#c=0
l1=[]
v='aeiou'
for i in l:
    c=0
    for j in i:
        if j in v :
            c+=1
    l1.append(c)
l2=[]
for k in l1:
    if k==min(l1):
        l2.append(k)
print(len(l2))
            