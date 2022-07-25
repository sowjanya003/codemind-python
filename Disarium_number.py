n=int(input())
l=list(str(n))
s1=0
k=[]
for i in range(len(l)):
    l[i]=int(l[i])
    s1=l[i]**(i+1)
    k.append(s1)
s1=sum(k)
if n==s1:
    print('True')
else:
    print('False')