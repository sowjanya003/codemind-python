n=int(input())
s=n*n
sum1=0
sum2=0
while(n>0):
    w=n%10
    sum1=sum1*10+w
    n=n//10
s1=sum1*sum1
#print(s,s1,sum1,sum2)
ss=str(s)
l=list(ss)
rev=l[::-1]
ss1=str(s1)
l1=list(ss1)
if l1==rev:
    print('True')
else:
    print('False')