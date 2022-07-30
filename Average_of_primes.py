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
s=0
for i in range(len(l)):
    if prime(l[i]):
        c+=1
        s+=l[i]
avg=s/c
print('%0.2f'%avg)