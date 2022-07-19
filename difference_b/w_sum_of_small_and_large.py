n=input()
x=list(n.split())
l=[]
l1=[]
l2=[]
i=0
for i in x:
    for j in i:
        y=ord(j)
        l.append(y)
    l1.append(max(l))
    l2.append(min(l))
    #print(l1,l2)
    l.clear()
#print(l1,l2)
s1=sum(l1)
s2=sum(l2)
print(s1-s2)

    

        
        