n=input()
s=list(n.split())
l=[]
v="aeiou"
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
#print(l)
k=min(l)
e=l.count(k)
print(e)