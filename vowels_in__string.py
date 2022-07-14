n=input()
v='aeiouAEIOU'
l=[]
for i in n:
    if i in v and i in n:
        if i not in l:
            l.append(i)
print(*l)