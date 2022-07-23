def pl(i):
    p=i.lower()
    l=p[::-1]
    if p==l:
        return True
    else:
        return False
n=input()
l=n.split()
c=0
for i in l:
    if pl(i)==True:
        c+=1
print(c)
