from math import sqrt
def isprime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range (2,sq+1):
        if n%i==0:
            return False
    return True
        

p=int(input())
q=int(input())
c=0
for i in range(p,q+1):
    if isprime(i):
        c+=1
if c==0:
    print(-1)
else:
    print(c)

    
    