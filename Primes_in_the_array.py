def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
        
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if prime(i):
        c+=1
print(c)
    