n=int(input())
s=str(n)
l1=len(s)
l2=len(set(s))
if l1==l2:
    print('Unique Number')
else:
    print('Not Unique Number')
