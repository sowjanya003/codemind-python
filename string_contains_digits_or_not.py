n=int(input())
for i in range(n):
    x=input()
    l=list(x)
    num='0123456789'
    c=0
    for i in l:
        if i in num:
            c+=1
    if c!=0:
        print('Yes')
    else:
        print('No')
        