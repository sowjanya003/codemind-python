def su(a,b):
    s=a+b
    return s
x=int(input())
for i in range(x+1):
    m,n=map(int,input().split())
    print(su(m,n))

