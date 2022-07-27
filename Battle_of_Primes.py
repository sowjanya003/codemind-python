from math import *
def isprime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range (2,sq+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
m=int(input())
s1=n+m
s2=n+m+1
while isprime(s2)==False:
    s2+=1
print(s2-s1)