def pal(n):
    s=0
    t=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if(s==t):
        return True
    else:
        return False
t=int(input())
print(pal(t))