n=list(input())
l=[]
for i in n:
    if i not in l:
        l.append(i)
if l==n:
    print('True')
else:
    print('False')