def prime(n):
    if n==1:
        return 0
    for i in range(2,n//2+1):
        if i%n==0:
            return 0
    return 1

x=int(input())
c=0
for n in range(1,x):
    if x%n==0:
        if prime(n):
            print(n,end=' ')
            c+=1
if c==0:
    print('-1')