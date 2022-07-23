n=int(input())
l=list(map(int,input().split()))
t=[]
for i in l:
    t.append(i)

t.sort()
t.reverse()

if t==l:
    print('yes')
else:
    print('no')