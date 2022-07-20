s1=list(input().lower())
s2=list(input().lower())
s=""
l=[]
for i in s1:
    if i not in s2 and i not in s and i!=" ":
        s+=i
        if i not in l:
            l.append(i)
for i in s2:
    if i not in s1 and i not in s and i!=" ":
        s+=i
        if i not in l:
            l.append(i)
if len(l)!=0:
    l.sort()
    print(''.join(l))
else:
    print('-1')