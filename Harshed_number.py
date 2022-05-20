n=int(input())
s=0
m=n
while m>0:
    s=s+m%10
    m=m//10
if(n%s==0):
    print("True")
else:
    print("False")