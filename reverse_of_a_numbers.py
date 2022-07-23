def rev(a):
    r=0
    while(a):
        d=a%10
        r=r*10+d
        a//=10
    return r


a=int(input())
print(rev(a))