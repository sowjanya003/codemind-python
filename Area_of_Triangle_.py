a,b,c=map(int,input().split())
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**(1/2)
print('%0.2f'%a)