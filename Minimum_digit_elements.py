n=int(input())
l=list(map(int,input().split()))
c=0
a=min(l)
#print(l,len(str(a)))
'''while a>0:
    a//=10
    c+=1
print(str(c))
'''
for i in l:
    if len(str(a))==len(str(i)):
        c+=1
print(c)