n=input()
s=list(n.split())
l=[]
for k in range(len(s)):
    for i in s[k]:
        x=ord(i)
        l.append(x)
        y=abs(min(l)-max(l))
        k+=1
    print(y,end=' ')
    l.clear()