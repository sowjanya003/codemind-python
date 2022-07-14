n=input()
v='aeiouAEIOU'
l=[]
for i in n:
    if i in v:
        l.append(i)
if len(l)==0:
    print(0)
else:
    print(len(l))